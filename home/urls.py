
from django.contrib import admin

from django.urls import path, include

app_name = "home"

urlpatterns = [
    path('index', views.index.as_view(), name="index"),
]


