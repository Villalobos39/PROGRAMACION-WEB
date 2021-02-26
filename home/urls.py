
from django.urls import path

app_name = "home"

urlpatterns = [
    path('index', views.index.as_view(), name="index"),
]
