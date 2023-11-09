from django.db import models
class Candidato(models.Model):
    nombre = models.CharField(max_length=100)
    seguidores = models.IntegerField()
    favoritos = models.IntegerField()
    numero_listas = models.IntegerField()
    p_seguidores = models.FloatField()
    p_favoritos = models.FloatField()
    p_listas = models.FloatField()

def _str_(self):
    return self.nombre