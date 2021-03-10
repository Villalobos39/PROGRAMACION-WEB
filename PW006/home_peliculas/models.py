from django.db import models

# Create your models here.
class Pelis(models.Model):
    nombre = models.CharField(max_length=30)
    Genero = models.CharField(max_length=30)
    Estreno = models.CharField(max_length=30)
    Comentario = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre