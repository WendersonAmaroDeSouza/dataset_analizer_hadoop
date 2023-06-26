# Word Sentiment Analizer With Twitter Dataset

O projeto de análise de média de sentimentos de palavras é uma solução completa que utiliza várias tecnologias para processar e analisar um conjunto de dados de tweets do Twitter. A arquitetura do projeto é baseada em Docker, Ansible, Terraform, Hadoop, GCP, Django e Python, e envolve várias etapas para realizar a análise.

Inicialmente, o projeto utiliza o Terraform para provisionar e configurar um cluster Hadoop na plataforma Google Cloud Platform (GCP). O Ansible é responsável pela configuração e gerenciamento do cluster, garantindo que todos os componentes necessários estejam corretamente instalados e configurados.

Após a configuração do cluster, é realizado o carregamento de um conjunto de dados de tweets no Hadoop. Esse conjunto de dados servirá como entrada para a análise de sentimentos. O carregamento é realizado por meio de jobs de mapeamento e redução (mapper/reducer) em Python, que são executados no cluster Hadoop. Esses jobs são responsáveis por processar e extrair informações relevantes dos tweets, como palavras-chave e sentimentos associados.

Uma vez concluída a análise dos tweets, os resultados são disponibilizados em um banco de dados SQLite. A integração com o banco de dados é feita por meio do Django, um framework web em Python. O Django é responsável por criar uma API que permite o acesso aos resultados da análise de sentimentos.

Dessa forma, os usuários podem consumir os dados via API do Django, obtendo informações sobre a média de sentimentos associada a palavras-chave específicas nos tweets analisados.

O projeto é uma solução abrangente que combina tecnologias de nuvem, processamento distribuído, processamento de dados, análise de sentimentos e desenvolvimento web para oferecer uma plataforma completa de análise de dados de tweets com foco na avaliação de sentimentos.

Laboratório básico para a ferramenta [Hadoop](http://hadoop.org/) provisionado no Google Cloud Platform - GCP

## Web Interfaces

O cluster Hadoop estiver instalado e funcionando, verifique a interface do usuário da web dos componentes conforme descrito abaixo:

Service|url|Port
---|---|---
ResourceManager  | http://<<ip_master>>:port/ | Default HTTP port is 8088.

## Terraform

O Terraform irá instanciar 3 máquinas e compartilhar a chave pública do host com as máquinas virtuais, **deverá ter o nome "id_rsa.pub"**. Para passar as credenciais para o terraform basta popular a variável de ambiente **GOOGLE_APPLICATION_CREDENTIALS**.

```shell
  export GOOGLE_APPLICATION_CREDENTIALS=<path_json>
```

## Inicializar o Twitter Dataset Analizer

Clonar o projeto

```shell
git clone  https://github.com/WendersonAmaroDeSouza/distributed_computing_class
```

## Crie um novo projeto na GCP

## Crie um conta de serviço

## Crie um compute engine

## Exporte a chave

## Renomeie a chave para keyfile.json

Um dos passos necessários para utilizar esse _setup_ é possuir uma par de _keys_ SSH, podendo ser gerado através do seguinte comando, para mais detalhes consulte a documentação atrves desse [link](https://wiki.debian.org/SSH)

```shell
ssh-keygen
```

Essa chave deverá ser mapeada no docker-compose.yml da seguinte maneira

```
  ...
  ports:
    - '8000:8000'
    volumes:
    - '../.:/root/lab-hadoop'
    - '<ssh_keys_path>/.ssh:/root/.ssh' # troque <ssh_keys_path> pelo caminho que de acesso a suas chaves ssh
  ...
```

## Suba a ambiente com o docker compose

```shell
cd my_directory/distributed_computing_class/lab-hadoop/docker
docker compose up -d
```

Acesse o container lab-hadoop

```shell
docker exec -ti lab-hadoop /bin/bash
```

Após a geração da chave renomeie o arquivo [terraform/terraform.tfvars.sample](terraform/terraform.tfvars.sample) para terraform.tfvars (nesse arquivo irá conter todas as variáveis para criar as instâncias no GCP). Crie um [**service-accounts**](https://cloud.google.com/compute/docs/access/service-accounts) com uma chave do tipo **JSON** e exponha no ambiente através do variável _GCP_SERVICE_ACCOUNT_FILE_

Exportar as variáveis de ambiente

```shell
export GCP_SERVICE_ACCOUNT_FILE=/path/keyfile.json  && \
export GOOGLE_APPLICATION_CREDENTIALS=/path/keyfile.json
```

Para inicializar os modulos, execute o seguinte comando:

```shell
# /root/lab-hadoop/terraform/
terraform init
```

Para verificar se os arquivos possui algum erro de sintaxe ou de configuração das instâncias execute o seguinte comando:

```shell
# /root/lab-hadoop/terraform/
terraform plan
```

Após a verificação do _plan_ execulte o seguinte comando para realizar o processo de instanciação

```shell
# /root/lab-hadoop/terraform/
terraform apply
```

Se tudo estiver ok a saída será similar a esta:

```text
Apply complete! Resources: 7 added, 0 changed, 0 destroyed.

Outputs:

manager_public = [
  "<<ip_public>>",
]
worker_internal = [
  "<<ip_internal1>>",
  "<<ip_internal1>>"
]
```

## Ansible

Para realizar a configuração do ambiente será necessrio que esteja populada a variável de ambiente **GCP_SERVICE_ACCOUNT_FILE**

```shell
  export GCP_SERVICE_ACCOUNT_FILE=<path_json>/keyfile.json
```

### Executar o Ansible

Para execultar o Ansible será necessário realizar o download do plugin **gce_compute**:

```shell
  pip3 install requests google-auth
```

Crie os arquivos `inventory.gcp.yml` e `playbook.yml`, utilize os exemplos.

Para inicializar o Ansible:

```shell
# /root/lab-hadoop/ansible/
ansible-playbook -i inventory.gcp.yml -u gce  playbook.yml
```
## Exemplo

Para executar uma aplicação Hadoop deverá ser criado um diretório no qual será gerado uma pasta de saída, a pasta de saída **não pode existir**.

```shell
hdfs namenode -format
```

Inicialize os serviços:

```shell
start-dfs.sh
start-yarn.sh
```

Para executar uma aplicação Hadoop deverá ser criado um diretorio no qual será gerado uma pasta de saída, a pasta de saída **não pode existir**.

```shell
mkdir input
cp $HADOOP_COMMON_HOME/etc/hadoop/*.xml input
```

Copiar o diretório input para o HDFS

```shell
hadoop dfs -copyFromLocal input /in
```

Execultar o WordCount

```shell
hadoop jar $HADOOP_COMMON_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.2.jar wordcount /in output
```

Coletar a saída do HDFS

```shell
hdfs dfs -get output output
cat output/*
```

# Twitter Sentiments

## Descubra os sentimentos de cada palavra bom base em Twitters

### Terraform

- Inicie o Terraform

```shell 
/lab-hadoop/terraform/terraform init 
``` 

- Verifique o que será aplicado no ambiente remoto

```shell 
/lab-hadoop/terraform/terraform plan
``` 

- Aplique ao ambiênte remoto

```shell 
/lab-hadoop/terraform/terraform apply
``` 

### Ansible

- Aplique as tasks do Ansible ao ambiente remoto

```shell 
cd /lab-hadoop/terraform/ansible
/lab-hadoop/ansible/ ansible-playbook -i inventory.gcp.yml -u gce playbook.yml
``` 

### Dataset Analizer

O dataset analizer será o responsável por comunicar com o cluster hadoop. Ele carregará o dataset para o hdfs e executará 
o mapper reduccer do job selecionado a partir do `job_executor.py`

- Execute o job_executor.py

```shell
cd root/lab-hadoop/dataset-analizer
python3 job_executor.py
```

Ao executar as seguintes ações serão disparadas

  - 

### GCP

- Executar o mapper-reducer-job para verificar o sentimento médio de cada palavra com base nos Twitter no dataset

```shell 
$HADOOP_HOME/bin/hdfs dfs -mkdir /in
``` 

```shell 
$HADOOP_HOME/bin/hdfs dfs -mkdir /out
``` 

- Carregar o dataset no hdfs

```shell 
$HADOOP_HOME/bin/hdfs dfs -put /home/hadoop/twitter_dataset.csv /in 
``` 

- Para analizar as palavras do dataset execute o mapper reducer job da seguinte maneira

```shell 
$HADOOP_HOME/bin/mapred streaming -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input /user/hadoop/input -output /user/hadoop/output 
``` 

- Para realizar o download da saída do Mapreduce

```shell 
$HADOOP_HOME/bin/hdfs dfs -get /user/hadoop/output 
``` 
 
