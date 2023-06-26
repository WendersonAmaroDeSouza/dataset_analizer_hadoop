from django.db import models

class DadosCSV(models.Model):
    coluna1 = models.CharField(max_length=100)
    coluna2 = models.CharField(max_length=100)
    coluna3 = models.CharField(max_length=100)
