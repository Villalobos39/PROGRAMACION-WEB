from django.db import models

# Create your models here.
class Pelis(models.Model):
    nombre = models.CharField(max_length=30)
    Genero = models.CharField(max_length=30)
    Estreno = models.CharField(max_length=30)
    Comentario = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre