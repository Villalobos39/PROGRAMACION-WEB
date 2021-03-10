from django.db import models

# Create your models here.

class OnePiece(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    correo = models.EmailField()
    nacionalidad = models.CharField(max_length=30)

    def _str_(self):
        return self.nombre
