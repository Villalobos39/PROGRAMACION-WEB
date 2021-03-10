from django.db import models

# Create your models here.
class Musica(models.Model):
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    duracion = models.CharField(max_length=30)
    artista = models.CharField(max_length=10)

    def _str_(self):
        return self.nombre