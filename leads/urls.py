from django.urls import path
from leads import views

app_name = "leads"

urlpatterns = [
    path('list_leads/', views.ListLeadsView.as_view(), name="list_leads"),
]