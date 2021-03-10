from django.shortcuts import render

# Create your views here.
from django.views import  generic 

from .models import Lead


class ListLeadsView(generic.ListView):
    template_name = "leads/list_leads.html"
    model = Lead
  
