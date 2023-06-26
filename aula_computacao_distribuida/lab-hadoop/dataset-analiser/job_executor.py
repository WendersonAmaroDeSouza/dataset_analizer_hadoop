import mapper_reducer_jobs
import pkgutil
import mapper_reducer_jobs
from hadoop_api.api import HadoopClient
import subprocess
import os

hdc = HadoopClient()

def get_mapper_reducer_jobs():
    package_path = mapper_reducer_jobs.__path__[0]
    package_name = mapper_reducer_jobs.__name__
    submodules = {}

    for module_info in pkgutil.walk_packages([package_path], f"{package_name}."):
        module_name = module_info.name
        parts = module_name.split('.')
        submodule = parts[-1]
        parent_module = '.'.join(parts[:-1])
        
        if parent_module not in submodules:
            submodules[parent_module] = []
        
        submodules[parent_module].append(submodule)

    return submodules

def exec_mapper_reducer_job(job_name, dataset_path, output_path):
    job_path = f'mapper_reducer_jobs/{job_name}'
    hdfs_input_path = '/input'
    hdfs_output_path = '/output'
    hdc.upload(f'{job_path}/mapper.py', './')
    hdc.upload(f'{job_path}/reducer.py', './')
    hdc.exec_hdfs_command(f'hdfs dfs -rm -r -skipTrash {hdfs_input_path}')
    hdc.exec_hdfs_command(f'hdfs dfs -rm -r -skipTrash {hdfs_output_path}')
    hdc.upload_to_hdfs(dataset_path, hdfs_input_path)
    print(f'Hdfs Command: mapred streaming -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input {hdfs_input_path} -output {hdfs_output_path}')
    hdc.exec_hdfs_command(f'mapred streaming -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input {hdfs_input_path} -output {hdfs_output_path}')
    hdc.download_from_hdfs(hdfs_output_path, output_path)

def test_mapper_reducer_job(job_name, dataset_path, output_path):
    job_path = f'mapper_reducer_jobs/{job_name}'
    mapper_path = f'/root/lab-hadoop/dataset-analiser/{job_path}/mapper.py'
    reducer_path = f'/root/lab-hadoop/dataset-analiser/{job_path}/reducer.py'
    hdc.convert_files_to_unix_format(mapper_path)
    hdc.convert_files_to_unix_format(reducer_path)
    command = f'cat {dataset_path} | {mapper_path} | sort -k1,1 | {reducer_path}'
    print(f'Command: {command}')
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if output:
        print("Saída:", output.decode())
    if error:
        print("Erro:", error.decode())

exec_mapper_reducer_job('word_sentiment', '/root/lab-hadoop/twitter_dataset.csv', 'output')
# test_mapper_reducer_job('word_sentiment', '/root/lab-hadoop/twitter_dataset.csv', 'output')
