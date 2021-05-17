from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.
# Create your views here.
from home_peliculas.models import Pelis
from home_peliculas.forms import LeadForm, UpdateLeadForm


class ListRegistView(generic.ListView):
    template_name = "home/list_regist.html"
    model = Pelis

 ## DETALLES   
class DetailLeadView(generic.DetailView):
    template_name = "home/detail_leads.html"
    model = Pelis
## CREAR NUEVO
class CreateLeadView(generic.CreateView):
    template_name = "home/create_leads.html"
    model = Pelis
    form_class = LeadForm
    success_url = reverse_lazy("home_peliculas:list_regist") 

## ACTUALIZAR   
class UpdateLeadView(generic.UpdateView):
    template_name = "home/update_leads.html"
    model = Pelis
    form_class = UpdateLeadForm
    success_url = reverse_lazy("home_peliculas:list_regist") 

## ELIMINAR
class DeleteLeadView(generic.DeleteView):
    template_name = "home/delete_leads.html"
    model = Pelis
    success_url = reverse_lazy("home_peliculas:list_regist")     





