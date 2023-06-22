# import findspark # Local Spark
# import subprocess
# import dataset_api as dst
# 
# # findspark.init(‘/home/cloudera/miniconda3/envs/<your_environment_name>/lib/python3.7/site-packages/pyspark/’)# Cloudera Cluster Spark
# # findspark.init(spark_home='/root/lab-hadoop')
# 
# 
# # Iniciar o DFS
# dfs_command = ['start-dfs.sh']
# subprocess.run(dfs_command, check=True)
# 
# # Iniciar o YARN
# yarn_command = ['start-yarn.sh']
# subprocess.run(yarn_command, check=True)
# 
# # Format namenode
# command = ['hdfs', 'namenode', '-format']
# subprocess.run(command, check=True)
# 
# # Load tweeter file to hdfs
# dst.load_tweetis_example()

import pyspark 
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
import pandas as pd
from datetime import datetime, date
from pyspark.sql import Row

# spark = SparkSession.builder\
#     .remote("sc://34.123.178.200:9000")\
#     .getOrCreate()

spark = SparkSession.builder\
    .master("local").appName("hdfs_test").getOrCreate()
    

def read_from_hdfs():
    booksSchema = StructType()\
        .add("id", "integer")\
        .add("book_title", "string")\
        .add("publish_or_not", "string")\
        .add("technology", "string")

    booksdata = spark.read.csv("hdfs://34.123.178.200/in", schema=booksSchema)
    booksdata.show(5)
    booksdata.printSchema()

def write_to_hdfs():
    local_csv_path = '/root/lab-hadoop/twitter_dataset.csv'
    remote_hdfs_path = '/in'
    df = spark.read.csv(local_csv_path, header=True, inferSchema=True)
    df.write.csv(remote_hdfs_path, mode='overwrite')

def save_dataframe():

    df = spark.createDataFrame([
        Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
        Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
        Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
    ])
    df.show()

    df.write.csv('foo.csv', header=True)

# write_to_hdfs()
# read_from_hdfs()

save_dataframe()
