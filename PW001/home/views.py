from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.
from .models import OnePiece
from .forms import LeadForm, UpdateLeadForm

class ListRegistView(generic.ListView):
    template_name = "home/list_regist.html"
    model = OnePiece
  
class Index(generic.TemplateView):
 template_name = "home/index.html"
   ## template_name = "base/base.html"

  
#  def get(self, request):
#     numbers = [i for i in range(10)]
#     context ={
#         'message': "VILLALOBS PEREZ DULCE JASMIN" ,
#         'numbers': numbers,
#     }
#     return render(request, "home/index.html", context)

## DETALLES   
class DetailLeadView(generic.DetailView):
    template_name = "home/detail_leads.html"
    model = OnePiece
## CREAR NUEVO
class CreateLeadView(generic.CreateView):
    template_name = "home/create_leads.html"
    model = OnePiece
    form_class = LeadForm
    success_url = reverse_lazy("home:list_regist") 

## ACTUALIZAR   
class UpdateLeadView(generic.UpdateView):
    template_name = "home/update_leads.html"
    model = OnePiece
    form_class = UpdateLeadForm
    success_url = reverse_lazy("home:list_regist") 

## ELIMINAR
class DeleteLeadView(generic.DeleteView):
    template_name = "home/delete_leads.html"
    model = OnePiece
    success_url = reverse_lazy("home:list_regist")    
