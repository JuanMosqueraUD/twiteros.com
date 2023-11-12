from django.db import models #se importa models para poder crear la clase Candidato
class Candidato(models.Model): #se crea la clase Candidato
    nombre = models.CharField(max_length=100)
    seguidores = models.IntegerField()
    favoritos = models.IntegerField()
    numero_listas = models.IntegerField()
    p_seguidores = models.FloatField()
    p_favoritos = models.FloatField()
    p_listas = models.FloatField()

def __str__(self): #se crea la funcion __str__ para que al momento de llamar a un objeto de la clase Candidato, se muestre el nombre del candidato
        return self.nombre 
#anteriormente las lineas de barras bajas solo tenian una, cuando tenian q ser 2, lo cual parece que no afectaba pero igual estaba mal