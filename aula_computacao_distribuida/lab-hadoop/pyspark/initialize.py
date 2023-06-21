import findspark # Local Spark
import subprocess
import dataset_api as dst

# findspark.init(‘/home/cloudera/miniconda3/envs/<your_environment_name>/lib/python3.7/site-packages/pyspark/’)# Cloudera Cluster Spark
# findspark.init(spark_home='/root/lab-hadoop')


# Iniciar o DFS
dfs_command = ['start-dfs.sh']
subprocess.run(dfs_command, check=True)

# Iniciar o YARN
yarn_command = ['start-yarn.sh']
subprocess.run(yarn_command, check=True)

# Format namenode
command = ['hdfs', 'namenode', '-format']
subprocess.run(command, check=True)

# Load tweeter file to hdfs
dst.load_tweetis_example()
