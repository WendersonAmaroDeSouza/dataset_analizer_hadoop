import subprocess

local_dir = '/path/to/local/input'
hdfs_dir = '/in'

def load_tweetis_example():
    local_dir = '/lab-hadoop/twitter_dataset.csv'
    hdfs_dir = '/in'
    load_to_hdfs(local_dir, hdfs_dir)

def load_to_hdfs(local_dir, hdfs_dir):
    command = ['hadoop', 'dfs', '-copyFromLocal', local_dir, hdfs_dir]
    subprocess.run(command, check=True)
