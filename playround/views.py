from django.shortcuts import render
from django.http import HttpResponse
from playround.TwitterReto import *
# Create your views here.





def datos(request):
    candidatos = Candidato.objects.all()
    return render(request, 'index.html', {'candidatos': candidatos})