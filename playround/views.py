from django.shortcuts import render
from django.http import HttpResponse
from playround.TwitterReto import *
# Create your views here.

def datos(request): #se crea la funcion datos para que al momento de llamar a la pagina principal, se muestren los datos de los candidatos
    crear_candidatos_desde_dataframe() #se llama a la funcion crear_candidatos_desde_dataframe para que se creen los candidatos en la base de datos
    candidatos = Candidato.objects.all() #se crea la variable candidatos para que guarde todos los candidatos de la base de datos
    return render(request, 'index.html', {'candidatos': candidatos}) #se retorna la pagina index.html con los candidatos