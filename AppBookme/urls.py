from django.contrib import admin
from django.urls import path
from AppBookme.views import inicio

urlpatterns = [
    path('', inicio, name="Inicio"),
]
