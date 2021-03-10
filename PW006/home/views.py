from django.shortcuts import render
from django.views import generic
# Create your views here.

class Index(generic.TemplateView):
 template_name = "home/index.html"
   ## template_name = "base/base.html"

  
 def get(self, request):
    numbers = [i for i in range(10)]
    context ={
        'message': "VILLALOBS PEREZ DULCE JASMIN" ,
        'numbers': numbers,
    }
    return render(request, "home/index.html", context)
