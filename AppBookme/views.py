from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from AppBookme.models import Autores, Genero, Libro, Editoriales, Reseñas

# Libros
def inicio(req):
    return render(req, "inicio.html", {})

class LibrosLista(ListView):
	model = Libro
	template_name = "lista_libros.html"#'ListaLibros'
	context_object_name = "libros"

class LibrosDetalles(DetailView):
	model = Libro
	template_name = "detalle_libro.html"#'DetalleLibro'
	context_object_name = "libros"

class LibroFormulario(CreateView):
	model = Libro
	template_name = "formulario_libro.html"#'FormularioLibro'
	success_url = reverse_lazy('ListaLibros')
	fields = ['titulo', 'autor', 'genero', 'publicacion', 'sinopsis']

class LibroEditar(UpdateView):
	model = Libro
	template_name = "editar_libro.html"#'EditarLibro'
	success_url = reverse_lazy('ListaLibros')
	fields = ['titulo', 'autor', 'genero', 'publicacion', 'reseña']

class LibroEliminar(DeleteView):
	model = Libro
	template_name = "eliminar_libro.html"#'EliminarLibro'
	success_url = reverse_lazy('ListaLibros')

def busquedaLibro(req):
	return render(req, "resultadoBusqueda.html")

def buscar(req):
	try:
		if req.GET["libro"]:
			libro = req.GET["libro"]
			libros =Libro.objects.filter(titulo__icontains=libro)
			return render(req, "resultadoBusqueda.html", {"libros":libros})
		else:
			return render(req, "resultadoBusqueda.html", {"mensaje":"Ingrese un Titulo"})
	except:
		return render(req, "resultadoBusqueda.html", {"mensaje":"Libro no encontrado"})

#Autores

class AutoresLista(ListView):
	model = Autores
	template_name = "lista_autores.html"#'ListaAutores'
	context_object_name = "autor"

class AutoresDetalles(DetailView):
	model = Autores
	template_name = "detalle_autores.html"#'DetalleAutores'
	context_object_name = "autor"

class AutoresFormulario(CreateView):
	model = Autores
	template_name = "formulario_autores.html"#'FormularioAutores'
	success_url = reverse_lazy('ListaAutores')
	fields = ['nombre', 'apellido', 'nacionalidad']

class AutoresEditar(UpdateView):
	model = Autores
	template_name = "editar_autores.html"#'EditarAutores'
	success_url = reverse_lazy('ListaAutores')
	fields = ['nombre', 'apellido', 'nacionalidad']

class AutoresEliminar(DeleteView):
	model = Autores
	template_name = "eliminar_autor.html"#'EliminarAutores'
	success_url = reverse_lazy('ListaAutores')

def busquedaAutores(req):
	return render(req, "resultadoBusqueda.html")

def buscar(req):
	try:
		if req.GET["autor"]:
			autor = req.GET["autor"]
			autores =Autores.objects.filter(titulo__icontains=autor)
			return render(req, "resultadoBusqueda.html", {"autores":autores})
		else:
			return render(req, "resultadoBusqueda.html", {"mensaje":"Ingrese un Nombre"})
	except:
		return render(req, "resultadoBusqueda.html", {"mensaje":"Autores no encontrado"})

#Generos

#Editoriales

#Reseñas