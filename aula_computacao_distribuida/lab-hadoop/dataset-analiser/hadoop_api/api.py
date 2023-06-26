from .base_api import BaseHadoopClient
import time
import random
import os

class HadoopClient(BaseHadoopClient):
    def __init__(self):
        super().__init__()
        self.connect_to_hadoop_server()

    def upload(self, local_path, remote_path):
        self.exec_command(f'mkdir -p {remote_path}')
        print(f'Remote Temp Directory: {remote_path}')
        self.exec_sftp_upload(local_path, f'{remote_path}/{os.path.basename(local_path)}')

    def download(self, remote_path, local_path):
        self.exec_sftp_download(remote_path, local_path)

    def upload_to_hdfs(self, local_path, hdfs_path):
        remote_dir = f'/tmp/upload/{time.time()}{random.getrandbits(128)}'
        self.upload(local_path, remote_dir)
        self.exec_hdfs_command(f'hadoop fs -moveFromLocal {remote_dir}/{os.path.basename(local_path)} {hdfs_path}')
        # self.exec_command(f'rm -R {remote_dir}')
        print(f'Copy {local_path} to {hdfs_path} hdfs path')
    
    def download_from_hdfs(self, hdfs_path, local_path):
        remote_dir = f'/tmp/download/{time.time()}{random.getrandbits(128)}'
        self.exec_command(f'mkdir -p {remote_dir}')
        print(f'Remote Temp Directory: {remote_dir}')
        self.exec_hdfs_command(f'hadoop fs -get {hdfs_path} {remote_dir}')
        print('Okayy')
        self.download(remote_dir, local_path)
        print(f'Copy {hdfs_path} hdfs path to {local_path}')

# Exemplo de uso da classe HadoopClient
# hadoop_client = HadoopClient()
# hadoop_client.connect_to_hadoop_server()
# 
# local_file = '/root/lab-hadoop/twitter_dataset.csv'
# hdfs_path = '/in'
# 
# hadoop_client.upload_to_hdfs(local_file, hdfs_path)
# hadoop_client.download_from_hdfs(hdfs_path, 'output')
# 
# hadoop_client.close_connection()
