from django.db import models

# Create your models here.
class Paisajes(models.Model):
    nombre = models.CharField(max_length=30)
    Lugar = models.CharField(max_length=30)
    turismo = models.CharField(max_length=30)
    artifical_natural = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre