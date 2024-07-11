from . import views
from django.urls import path,include


urlpatterns = [
    path("", views.index, name='index'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
   
]