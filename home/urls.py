from django.urls import path

from home import views

app_name = "home"

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('list/', views.list, name="list"),
    # path('listusers/', views.ListUsers.as_view(), name="listusers"),
]
