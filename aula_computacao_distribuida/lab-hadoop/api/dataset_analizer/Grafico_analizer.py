from django.shortcuts import render

from django.http import JsonResponse
from .models import DadosCSV
import matplotlib.pyplot as plt
import datetime


def api_dados_csv(request):
    dados_csv = DadosCSV.objects.all()

# Datas para o eixo X
datas = [
    datetime.date(2023, 6, 1),
    datetime.date(2023, 6, 5),
    datetime.date(2023, 6, 10),
    datetime.date(2023, 6, 15),
    datetime.date(2023, 6, 20)
]

# Valores para o eixo Y
valores = [10, 15, 8, 12, 9]

# Plotar o gráfico
plt.plot(datas, valores)

# Configurar o formato das datas no eixo X
plt.gca().xaxis.set_major_formatter(plt.DateFormatter('%Y-%m-%d'))

# Rotacionar as datas para melhor visualização
plt.gcf().autofmt_xdate()

# Exibir o gráfico
plt.show()
 
return JsonResponse(plt.show())
