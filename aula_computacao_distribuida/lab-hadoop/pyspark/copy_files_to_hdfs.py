import pydoop.hdfs as hdfs

# Local file path
local_file = '/root/lab-hadoop/twitter_dataset.csv'

# Destination path in HDFS
hdfs_path = '/input/twitter_dataset.csv'

# Copy file to HDFS
with hdfs.open(hdfs_path, 'w') as hdfs_file:
    with open(local_file, 'rb') as local:
        hdfs_file.write(local.read())

print("File copied to HDFS.")
