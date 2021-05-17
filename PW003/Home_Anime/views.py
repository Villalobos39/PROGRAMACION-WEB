from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
from Home_Anime.models import Anime
from Home_Anime.forms import LeadForm, UpdateLeadForm

class ListRegistView(generic.ListView):
    template_name = "home/list_regist.html"
    model = Anime
  
## DETALLES   
class DetailLeadView(generic.DetailView):
    template_name = "home/detail_leads.html"
    model = Anime
## CREAR NUEVO
class CreateLeadView(generic.CreateView):
    template_name = "home/create_leads.html"
    model = Anime
    form_class = LeadForm
    success_url = reverse_lazy("Home_Anime:list_regist") 

## ACTUALIZAR   
class UpdateLeadView(generic.UpdateView):
    template_name = "home/update_leads.html"
    model = Anime
    form_class = UpdateLeadForm
    success_url = reverse_lazy("Home_Anime:list_regist") 

## ELIMINAR
class DeleteLeadView(generic.DeleteView):
    template_name = "home/delete_leads.html"
    model = Anime
    success_url = reverse_lazy("Home_Anime:list_regist")   