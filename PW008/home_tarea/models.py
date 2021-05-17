from django.db import models

# Create your models here.
class Tarea(models.Model):
    nombre = models.CharField(max_length=30)
    Materia = models.CharField(max_length=30)
    Fecha = models.CharField(max_length=30)
    Activuidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre