from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('index', views.Index.as_view(), name="index"),
]


