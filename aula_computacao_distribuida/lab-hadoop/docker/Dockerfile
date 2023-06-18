ARG VARIANT="bullseye"

FROM debian:${VARIANT} as develop-stage

ENV TERRAFORM_VERSION="1.0.4"

# Terraform Instalation Steps: https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli
RUN apt update && \
    apt upgrade && \
    apt install -y curl && \
    apt-get -y install gnupg && \ 
    apt install -y unzip && \
    apt install -y wget && \
    wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    mv terraform /usr/local/bin/ && \
    # curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - && \
    # apt-get install -y gnupg software-properties-common curl && \
    # apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com (lsb_release -cs) main" && \
    # apt update && \
    # apt-get install terraform && \
    # apt-get update && apt-get install -y gnupg software-properties-common && \
    #
    # wget -O- https://apt.releases.hashicorp.com/gpg | \
    # gpg --dearmor | \
    # tee /usr/share/keyrings/hashicorp-archive-keyring.gpg && \
    # gpg --no-default-keyring \
    # --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
    # --fingerprint && \
    # echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
    # https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
    # tee /etc/apt/sources.list.d/hashicorp.list && \
    # apt update && \
    # apt-get install terraform && \
    touch ~/.bashrc && \
    terraform -install-autocomplete

# Ansible Instalation Steps: https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-ansible-on-debian-11
RUN apt install -y ansible

RUN apt-get update && \
    apt-get install -y openssh-client

RUN ssh-keygen -t rsa -b 4096 -f /root/.ssh/id_rsa -N "" -C "your_email@example.com"

CMD ["/bin/bash"]
