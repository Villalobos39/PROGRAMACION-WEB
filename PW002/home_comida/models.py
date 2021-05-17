from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Create your models here.

 
class Comida(models.Model):
    Restaurante = models.CharField(max_length=30)
    Correo_Local = models.EmailField()
    nombre = models.CharField(max_length=30)
    cantidad = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
