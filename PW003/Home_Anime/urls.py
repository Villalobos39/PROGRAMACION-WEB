from django.urls import path
from Home_Anime import views

app_name = "Home_Anime"

urlpatterns = [
   # path('', views.Index.as_view(), name="index"),
    path('', views.ListRegistView.as_view(), name="list_regist"),
    path('detail_leads/<int:pk>/', views.DetailLeadView.as_view(), name="detail_leads"),
    path('create_leads/', views.CreateLeadView.as_view(), name="create_leads"),
    path('update_leads/<int:pk>/', views.UpdateLeadView.as_view(), name="update_leads"),
    path('delete_leads/<int:pk>/', views.DeleteLeadView.as_view(), name="delete_leads"),
]


