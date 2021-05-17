from django.urls import path
from home import views
from django.contrib.auth import views as auth_views

app_name = "home"

urlpatterns = [
    path('', views.Index.as_view(), name = "index"),
    path('lead/', views.ListLeadsView.as_view(), name="lead"),
    path('list_leads/', views.ListLeadsView.as_view(), name="list_leads"),
    path('detail_leads/<int:pk>/', views.DetailLeadView.as_view(), name="detail_leads"),
    path('create_leads/', views.CreateLeadView.as_view(), name="create_leads"),
    path('update_leads/<int:pk>/', views.UpdateLeadView.as_view(), name="update_leads"),
    path('delete_leads/<int:pk>/', views.DeleteLeadView.as_view(), name="delete_leads"),
    path('login/', auth_views.LoginView.as_view(template_name ="home/index.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name ="home/index.html"), name="logout"),
   ## path('register/', views.RegisterLeadView.as_view(), name="register"),
]
