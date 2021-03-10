from django.db import models

# Create your models here.


class Alumnos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    no_control = models.CharField(max_length=30)
    edad = models.CharField(max_length=10)

    def _str_(self):
        return self.nombre
