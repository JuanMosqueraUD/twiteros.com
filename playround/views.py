from django.shortcuts import render
from django.http import HttpResponse
from playround.TwitterReto import *
# Create your views here.



def datos(request):
    crear_candidatos_desde_dataframe()
    return render(request, 'index.html')