from django.contrib import admin

#from django.models
# Register your models here.

from .models import Comida
#admin.site.register()

admin.site.register(Comida)
