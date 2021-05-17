from django.db import models

# Create your models here.

class Bebida(models.Model):
    marca = models.CharField(max_length=30)
    precio = models.CharField(max_length=30)
    tienda = models.CharField(max_length=30)
    Vence = models.CharField(max_length=10)

    def __str__(self):
        return self.marca