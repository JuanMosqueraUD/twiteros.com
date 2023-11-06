from django.db import models

class Candidato(models.Model):
    nombre = models.CharField(max_length=100)
    seguidores = models.IntegerField()
    favoritos = models.IntegerField()
    porcentaje_seguidores = models.FloatField()
