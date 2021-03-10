from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre_Pais = models.CharField(max_length=30)
    Visitar = models.CharField(max_length=30)
    Trasnporte = models.CharField(max_length=30)
    
    def _str_(self):
        return self.nombre
