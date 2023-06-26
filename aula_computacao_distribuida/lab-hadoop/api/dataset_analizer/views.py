from django.shortcuts import render

from django.http import JsonResponse
from .models import DadosCSV

def api_dados_csv(request):
    dados_csv = DadosCSV.objects.all()

    data = []
    for dado in dados_csv:
        data.append({
            'coluna1': dado.coluna1,
            'coluna2': dado.coluna2,
            'coluna3': dado.coluna3
        })

    return JsonResponse(data, safe=False)
