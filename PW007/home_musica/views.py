from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.
from home_musica.models import Musica
from home_musica.forms import LeadForm, UpdateLeadForm

class Index(generic.TemplateView):
    template_name = "home/index.html" 

class ListRegistView(generic.ListView):
    template_name = "regist/list_regist.html"
    model = Musica

  ## DETALLES
class DetailLeadView(generic.DetailView):
    template_name = "home/detail_leads.html"
    model = Musica

## CREAR
class CreateLeadView(generic.CreateView):
    template_name = "home/create_leads.html"
    model = Musica
    form_class = LeadForm
    Success_url = reverse_lazy("regist:list_regist") 

## ACTUALIZAR  
class UpdateLeadView(generic.UpdateView):
    template_name = "home/update_leads.html"
    model = Musica
    form_class = UpdateLeadForm
    Success_url = reverse_lazy("regist:list_regist") 

## ELIMINAR
class DeleteLeadView(generic.DeleteView):
    template_name = "home/delete_leads.html"
    model = Musica  
    Success_url = reverse_lazy("regist:list_regist")      