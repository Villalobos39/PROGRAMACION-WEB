from django.db import models

# Create your models here.

class Anime(models.Model):
    genero = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    publicacion = models.CharField(max_length=30)
    temporadas = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
