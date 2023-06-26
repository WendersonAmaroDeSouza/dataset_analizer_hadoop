import csv
from dataset_analizer.models import DadosCSV

with open('/root/lab-hadoop/dataset-analiser/output/output/part-00000') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        dado = DadosCSV(
            coluna1=row['coluna1'],
            coluna2=row['coluna2'],
            coluna3=row['coluna3']
        )
        dado.save()
