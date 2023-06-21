# Eviroment Init

# Start Terraform and config works on GCP
cd /lab-hadoop/terraform
terraform init
terraform plan
terraform apply -auto-approve

# Start Ansible and config
apt install -y python3
apt install -y python3-pip
pip3 install requests google-auth

# Install Hadoop
apt install default-jdk default-jre -y
adduser hadoop
cp -R /root/.ssh /home/hadoop/.ssh
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
ssh Server's_IP_Address
