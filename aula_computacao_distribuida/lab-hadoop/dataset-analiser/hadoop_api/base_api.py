import paramiko
import configparser
import os
import time
import random
import stat
import subprocess

class BaseHadoopClient:
    def __init__(self):
        # Load configuration
        config = configparser.ConfigParser()
        config.read('/root/lab-hadoop/dataset-analiser/hadoop_api/config.ini')

        self.HOST = config.get('Server', 'host')
        self.PORT = config.getint('Server', 'port')
        self.USERNAME = config.get('Credentials', 'username')
        self.PASSWORD = config.get('Credentials', 'password')
        self.RSA_PRIVATE_PATH = config.get('Keys', 'rsa_private_path')
        self.HADOOP_PATH = config.get('Hadoop', 'hadoop_path')
        self.client = None

    def connect_to_hadoop_server(self):
        # Create SSH Client
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()

        RSAKey = paramiko.RSAKey.from_private_key_file(self.RSA_PRIVATE_PATH)

        self.client.connect(
            hostname=self.HOST, 
            username=self.USERNAME,
            pkey=RSAKey,
            allow_agent=True,
            look_for_keys=False
        )

    def convert_files_to_unix_format(self, file_path):
        if os.path.isdir(file_path):
            for sub_path in file_path:
                self.convert_files_to_unix_format(sub_path)
        else:
            try:
                subprocess.run(['dos2unix', file_path], check=True)
                print(f"Converted {file_path} from DOS to Unix format")
            except subprocess.CalledProcessError as e:
                print(f"Error converting {file_path}: {e}")

    def exec_sftp_upload(self, local_path, remote_path):
        self.convert_files_to_unix_format(local_path)
        scp = self.client.open_sftp()
        scp.put(local_path, remote_path)
    
    def exec_sftp_download(self, remote_path, local_path):
        scp = self.client.open_sftp()
        self._download_directory(scp, remote_path, local_path)

    def _download_directory(self, scp, remote_path, local_path):
        if not os.path.isdir(local_path):
            os.makedirs(local_path, exist_ok=True)

        for item in scp.listdir_attr(remote_path):
            remote_item_path = os.path.join(remote_path, item.filename)
            local_item_path = os.path.join(local_path, item.filename)
            if stat.S_ISDIR(item.st_mode):
                self._download_directory(scp, remote_item_path, local_item_path)
            else:
                scp.get(remote_item_path, local_item_path)

    def exec_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        time.sleep(0.5)
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')
        response = { 
            'output': output, 
            'error': error, 
            'stdin': stdin, 
            'stdout': stdout, 
            'stderr': stderr.read().decode('utf-8') 
        }
        return response
    
    def exec_hdfs_command(self, command):
        response = self.exec_command(f'{self.HADOOP_PATH}/{command}')
        return response
    
    def close_connection(self):
        if self.client is not None:
            self.client.close()

# Exemplo de uso da classe HadoopClient
hadoop_client = BaseHadoopClient()
hadoop_client.connect_to_hadoop_server()
# hadoop_client.change_to_hadoop_user('hadoop')
output = hadoop_client.exec_command('whoami').get('output')
print(f'Output: {output}')
time.sleep(2)
output = hadoop_client.exec_command('pwd').get('output')
print(f'Output: {output}')
output = hadoop_client.exec_command('jps').get('output')
print(f'Output: {output}')
out = hadoop_client.exec_hdfs_command('hadoop -h')
output = out.get('output')
error = out.get('error')
print(f'Output: {output}')
print(f'Error: {error}')
# hadoop_client.upload_to_hdfs('/path/to/hdfs', '/path/to/src')
# hadoop_client.close_connection()
