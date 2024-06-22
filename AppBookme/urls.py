from django.urls import path
from AppBookme.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('acerca-demi/', acercaDeMi, name="AcercaDeMi"),
    # Libros
    path('lista-libros/', LibrosLista.as_view(), name="ListaLibros"),
    path('detalle-libros/<pk>', LibrosDetalles.as_view(), name="DetalleLibro"),
    path('elimina-libros/<pk>', LibroEliminar.as_view(), name="EliminarLibro"),
    path('edita-libros/<pk>', LibroEditar.as_view(), name="EditarLibro"),
    path('formulario-libros/', libroFormulario, name="FormularioLibro"),
    path('busqueda-libro/', busquedaLibro, name = "BusquedaLibro"),
    path('busca-libros/', buscarLibro, name="BuscaLibros"),
    # Autores
    path('lista-autores/', AutoresLista.as_view(), name="ListaAutores"),
    path('detalle-autores/<pk>', AutoresDetalles.as_view(), name="DetalleAutores"),
    path('elimina-autores/<pk>', AutoresEliminar.as_view(), name="EliminarAutores"),
    path('edita-autores/<pk>', AutoresEditar.as_view(), name="EditarAutores"),
    path('formulario-autores/', autorFormulario, name="FormularioAutores"),
    path('busca-autores/', busquedaAutores, name="BusquedaAutores"),
    path('busca-autor/', buscarAutor, name="BuscaAutores"),
    #Generos
    path('lista-generos/', GenerosLista.as_view(), name="ListaGeneros"),
    path('detalle-generos/<pk>', GenerosDetalles.as_view(), name="DetalleGeneros"),
    path('elimina-generos/<pk>', GenerosEliminar.as_view(), name="EliminarGeneros"),
    path('edita-generos/<pk>', GenerosEditar.as_view(), name="EditarGeneros"),
    #Editoriales
    path('lista-editoriales/', EditorialesLista.as_view(), name="ListaEditoriales"),
    path('detalle-editoriales/<pk>', EditorialesDetalles.as_view(), name="DetalleEditoriales"),
    path('elimina-editoriales/<pk>', EditorialesEliminar.as_view(), name="EliminarEditoriales"),
    path('edita-editoriales/<pk>', EditorialesEditar.as_view(), name="EditarEditoriales"),
    path('detalle-libros/<int:libro_id>/reseña/', reseña_libro, name="Reseña"),
]
