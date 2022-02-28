from django.urls import path
from . import views


urlpatterns = [
    path('', views.ho, name = 'home-page'),
    path('todo', views.tas, name = 'todo'), 
    path('upadatetask/<str:pk>/', views.upadatetask, name = "update"),
    path('task/<str:pk>/', views.deletetask, name = "relde"),
    
]