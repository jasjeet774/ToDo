from . import views
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name='index'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
    
]