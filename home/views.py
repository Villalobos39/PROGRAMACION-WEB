from django.shortcuts import render
from django.views import generic
# Create your views here.

class Index(TemplateView):
    template_name = "home/index.html"

