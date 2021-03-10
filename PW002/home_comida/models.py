from django.db import models

# Create your models here.
# Create your models here.

class Comida(models.Model):
    Restaurante = models.CharField(max_length=30)
    Correo_Local = models.EmailField()
    nombre = models.CharField(max_length=30)
    cantidad = models.CharField(max_length=10)

    def _str_(self):
        return self.nombre
