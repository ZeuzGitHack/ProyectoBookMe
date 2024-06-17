from django.contrib import admin
from django.urls import path
from AppBookme.views import (
    inicio, 
    acercaDeMi,
    # Libros
    LibrosLista, 
    LibrosDetalles,
    LibroEditar,
    LibroEliminar,
    LibroFormulario
    )

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('acerca-demi/', acercaDeMi, name="AcercaDeMi"),
    path('lista-libros/', LibrosLista.as_view(), name="ListaLibros"),
    path('detalle-libros/<pk>', LibrosDetalles.as_view(), name="DetalleLibro"),
    path('elimina-libros/<pk>', LibroEliminar.as_view(), name="EliminarLibro"),
    path('edita-libros/<pk>', LibroEditar.as_view(), name="EditarLibro"),
    path('formulario-libros/<pk>', LibroFormulario.as_view(), name="FormularioLibro"),
]
