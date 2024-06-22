from django.urls import path
from AppBookme.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('acerca-demi/', acercaDeMi, name="AcercaDeMi"),
    # Libros
    path('lista-libros/', LibrosLista.as_view(), name="ListaLibros"),
    path('detalle-libros/<pk>', LibrosDetalles.as_view(), name="DetalleLibro"),
    path('elimina-libros/<int:id>', eliminar_libro, name="EliminarLibro"),
    path('edita-libros/<int:id>', editar_libro, name="EditarLibro"),
    path('formulario-libros/', libroFormulario, name="FormularioLibro"),
    path('busqueda-libro/', busquedaLibro, name = "BusquedaLibro"),
    path('busca-libros/', buscarLibro, name="BuscaLibros"),
    # Autores
    path('lista-autores/', AutoresLista.as_view(), name="ListaAutores"),
    path('detalle-autores/<pk>', AutoresDetalles.as_view(), name="DetalleAutores"),
    path('elimina-autores/<int:id>', eliminar_autor, name="EliminarAutores"),
    path('edita-autores/<int:id>', editar_autor, name="EditarAutores"),
    path('formulario-autores/', autorFormulario, name="FormularioAutores"),
    path('busca-autores/', busquedaAutores, name="BusquedaAutores"),
    path('busca-autor/', buscarAutor, name="BuscaAutores"),
    #Generos
    path('lista-generos/', GenerosLista.as_view(), name="ListaGeneros"),
    path('detalle-generos/<pk>', GenerosDetalles.as_view(), name="DetalleGeneros"),
    #Editoriales
    path('lista-editoriales/', EditorialesLista.as_view(), name="ListaEditoriales"),
    path('detalle-editoriales/<pk>', EditorialesDetalles.as_view(), name="DetalleEditoriales"),
    path('elimina-editoriales/<id>', eliminar_editorial, name="EliminarEditoriales"),
    path('edita-editoriales/<int:id>', editar_editorial, name="EditarEditoriales"),
    path('detalle-libros/<int:libro_id>/reseña/', reseña_libro, name="Reseña"),
]
