# Eviroment Init

# Start Terraform and config works on GCP
cd /root/lab-hadoop/terraform
terraform init
terraform plan
terraform apply -auto-approve

# Start Ansible and config
apt install -y python3
apt install -y python3-pip
pip3 install requests google-auth
chmod 700 /root/.ssh
chmod 600 /root/.ssh/config
chmod 600 /root/.ssh/id_rsa
ssh-keyscan 34.173.200.221 34.134.255.54 >> /root/.ssh/known_hosts
ansible-playbook -i inventory.gcp.yml -u gce playbook.yml

# Install Hadoop
apt install default-jdk default-jre -y
# adduser hadoop
# cp -R /root/.ssh /home/hadoop/.ssh
# ssh-keygen -t rsa
# cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
# chmod 0600 ~/.ssh/authorized_keys
# ssh Server's_IP_Address
