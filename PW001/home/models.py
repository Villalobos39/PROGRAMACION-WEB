from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
#

class OnePiece(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    correo = models.EmailField()
    nacionalidad = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
