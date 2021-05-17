from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from home.models import Lead, Agent
from .forms import LeadForm, UpdateLeadForm
# Create your views here.

class Index(generic.TemplateView):
    template_name = "home/index.html"
# 
class ListLeadsView(LoginRequiredMixin, generic.ListView):
    template_name = "home/list_leads.html"
    model = Lead
    login_url = "home:login"

## DETALLES   
class DetailLeadView(LoginRequiredMixin, generic.DetailView):
    template_name = "home/detail_leads.html"
    model = Lead
    login_url = "home:login"

## CREAR NUEVO
class CreateLeadView(LoginRequiredMixin, generic.CreateView):
    template_name = "home/create_leads.html"
    model = Lead
    form_class = LeadForm
    success_url = reverse_lazy("home:list_leads") 
    login_url = "home:login"

## ACTUALIZAR   
class UpdateLeadView(LoginRequiredMixin, generic.UpdateView):
    template_name = "home/update_leads.html"
    model = Lead
    form_class = UpdateLeadForm
    success_url = reverse_lazy("home:list_leads") 
    login_url = "home:login"

## ELIMINAR
class DeleteLeadView(LoginRequiredMixin, generic.DeleteView):
    template_name = "home/delete_leads.html"
    model = Lead
    success_url = reverse_lazy("home:list_leads")    
    login_url = "home:login"

# class RegisterLeadView(generic.CreateView):
#     template_name = "home/register.html"
#     model = Lead
