from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
from home_name.models import Alumnos
from home_name.forms import LeadForm, UpdateLeadForm

class ListRegistView(generic.ListView):
    template_name = "regist/list_regist.html"
    model = Alumnos
  

## DETALLES   
class DetailLeadView(generic.DetailView):
    template_name = "home/detail_leads.html"
    model = Alumnos
## CREAR NUEVO
class CreateLeadView(generic.CreateView):
    template_name = "home/create_leads.html"
    model = Alumnos
    form_class = LeadForm
    success_url = reverse_lazy("home_name:list_leads") 

## ACTUALIZAR   
class UpdateLeadView(generic.UpdateView):
    template_name = "home/update_leads.html"
    model = Alumnos
    form_class = UpdateLeadForm
    success_url = reverse_lazy("home_name:list_leads") 

## ELIMINAR
class DeleteLeadView(generic.DeleteView):
    template_name = "home/delete_leads.html"
    model = Alumnos
    success_url = reverse_lazy("home_name:list_leads")    