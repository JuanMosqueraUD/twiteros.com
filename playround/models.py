from django.db import models

class Candidato(models.Model):
    nombre = models.CharField(max_length=100)
    seguidores = models.IntegerField()
    favoritos = models.IntegerField()
    numero_listas = models.IntegerField()

    def __str__(self):
        return self.nombre
