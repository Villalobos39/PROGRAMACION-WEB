from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
from home_bebidas.models import Bebida
from home_bebidas.forms import LeadForm, UpdateLeadForm


class ListRegistView(generic.ListView):
    template_name = "home/list_regist.html"
    model = Bebida
  
  ## DETALLES   
class DetailLeadView(generic.DetailView):
    template_name = "home/detail_leads.html"
    model = Bebida
## CREAR NUEVO
class CreateLeadView(generic.CreateView):
    template_name = "home/create_leads.html"
    model = Bebida
    form_class = LeadForm
    success_url = reverse_lazy("home_bebidas:list_regist") 

## ACTUALIZAR   
class UpdateLeadView(generic.UpdateView):
    template_name = "home/update_leads.html"
    model = Bebida
    form_class = UpdateLeadForm
    success_url = reverse_lazy("home_bebidas:list_regist") 

## ELIMINAR
class DeleteLeadView(generic.DeleteView):
    template_name = "home/delete_leads.html"
    model = Bebida
    success_url = reverse_lazy("home_bebidas:list_regist")   