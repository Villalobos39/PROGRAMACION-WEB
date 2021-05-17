from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.
from .models import Pais
from .forms import LeadForm, UpdateLeadForm

class Index(generic.TemplateView):
    template_name = "regist/list_regist.html"

class ListRegistView(generic.ListView):
    template_name = "regist/list_regist.html"
    model = Pais
  
  ## DETALLES
class DetailLeadView(generic.DetailView):
    template_name = "home/detail_leads.html"
    model = Pais

## CREAR
class CreateLeadView(generic.CreateView):
    template_name = "home/create_leads.html"
    model = Pais
    form_class = LeadForm
    Success_url = reverse_lazy("regist:list_regist") 

## ACTUALIZAR  
class UpdateLeadView(generic.UpdateView):
    template_name = "home/update_leads.html"
    model = Pais
    form_class = UpdateLeadForm
    Success_url = reverse_lazy("regist:list_regist") 

## ELIMINAR
class DeleteLeadView(generic.DeleteView):
    template_name = "home/delete_leads.html"
    model = Pais
    Success_url = reverse_lazy("regist:list_regist")    