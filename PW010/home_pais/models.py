from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre_Pais = models.CharField(max_length=30)
    Visitar = models.CharField(max_length=30)
    Trasnporte = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
