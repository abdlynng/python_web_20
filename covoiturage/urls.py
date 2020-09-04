from django.urls import path
from . import views 

urlpatterns = [
    path('trajet/<int:pk>/', views.trajet, name='trajet'),
    path('conducteur/<int:pk>/', views.conducteur, name='conducteur'),
    path('', views.index, name='index'),
]

