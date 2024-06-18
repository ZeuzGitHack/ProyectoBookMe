from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from AppBookme.models import Autores, Genero, Libro, Editoriales, Reseñas

# Libros
def inicio(req):
    return render(req, "inicio.html", {})

def acercaDeMi(req):
    return render(req, "acerca_de_mi.html", {})

class LibrosLista(ListView):
	model = Libro
	template_name = "lista_libros.html"
	context_object_name = "libros"

class LibrosDetalles(DetailView):
	model = Libro
	template_name = "detalle_libro.html"
	context_object_name = "libro"

class LibroFormulario(CreateView):
	model = Libro
	template_name = "formulario_libro.html"
	success_url = reverse_lazy('ListaLibros')
	fields = ['titulo', 'autor', 'genero', 'publicacion', 'sinopsis']

class LibroEditar(UpdateView):
	model = Libro
	template_name = "editar_libro.html"
	success_url = reverse_lazy('ListaLibros')
	fields = ['titulo', 'autor', 'genero', 'publicacion', 'sinopsis']

class LibroEliminar(DeleteView):
	model = Libro
	template_name = "eliminar_libro.html"
	success_url = reverse_lazy('ListaLibros')

def busquedaLibro(req):
	return render(req, "resultadoBusqueda.html")

def buscarLibro(req):
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
	template_name = "lista_autores.html"
	context_object_name = "autor"

class AutoresDetalles(DetailView):
	model = Autores
	template_name = "detalle_autores.html"
	context_object_name = "autor"

class AutoresFormulario(CreateView):
	model = Autores
	template_name = "formulario_autores.html"
	success_url = reverse_lazy('ListaAutores')
	fields = ['nombre', 'apellido', 'nacionalidad']

class AutoresEditar(UpdateView):
	model = Autores
	template_name = "editar_autores.html"
	success_url = reverse_lazy('ListaAutores')
	fields = ['nombre', 'apellido', 'nacionalidad']
	context_object_name = "autor"

class AutoresEliminar(DeleteView):
	model = Autores
	template_name = "eliminar_autor.html"
	success_url = reverse_lazy('ListaAutores')
	context_object_name = "autor"

def busquedaAutores(req):
	return render(req, "resultadoBusqueda_autores.html")

def buscarAutor(req):
	try:
		if req.GET["autor"]:
			autor = req.GET["autor"]
			autores =Autores.objects.filter(nombre__icontains=autor)
			return render(req, "resultadoBusqueda_autores.html", {"autores":autores})
		else:
			return render(req, "resultadoBusqueda_autores.html", {"mensaje":"Ingrese un Nombre"})
	except:
		return render(req, "resultadoBusqueda_autores.html", {"mensaje":"Autores no encontrado"})

#Generos

class GenerosLista(ListView):
	model = Genero
	template_name = "lista_genero.html"
	context_object_name = "generos"

class GenerosDetalles(DetailView):
	model = Genero
	template_name = "detalle_genero.html"
	context_object_name = "genero"

class GenerosFormulario(CreateView):
	model = Genero
	template_name = "formulario_genero.html"
	success_url = reverse_lazy('ListaGeneros')
	fields = ['nombre', 'descripcion']

class GenerosEditar(UpdateView):
	model = Genero
	template_name = "editar_genero.html"
	success_url = reverse_lazy('ListaGeneros')
	fields = ['nombre', 'descripcion']

class GenerosEliminar(DeleteView):
	model = Genero
	template_name = "eliminar_genero.html"
	success_url = reverse_lazy('ListaGeneros')

#Editoriales

class EditorialesLista(ListView):
	model = Editoriales
	template_name = "lista_editoriales.html"
	context_object_name = "editoriales"

class EditorialesDetalles(DetailView):
	model = Editoriales
	template_name = "detalle_editoriales.html"
	context_object_name = "editorial"

class EditorialesFormulario(CreateView):
	model = Editoriales
	template_name = "formulario_editorial.html"
	success_url = reverse_lazy('ListaEditoriales')
	fields = ['nombre', 'pais', 'direccion', 'contacto', 'libros']

class EditorialesEditar(UpdateView):
	model = Editoriales
	template_name = "editar_editorial.html"
	success_url = reverse_lazy('ListaEditoriales')
	fields = ['nombre', 'pais', 'direccion', 'libros']

class EditorialesEliminar(DeleteView):
	model = Editoriales
	template_name = "eliminar_editorial.html"
	success_url = reverse_lazy('ListaEditoriales')

#Reseñas

class ReseñasFormulario(CreateView):
	model = Reseñas
	template_name = "crear_reseña.html"
	success_url = reverse_lazy('ListaLibros')
	fields = ['usuario', 'libro', 'comentario', 'fecha']

class ReseñasEditar(UpdateView):
	model = Reseñas
	template_name = "editar_editorial.html"
	success_url = reverse_lazy('ListaLibros')
	fields = ['usuario', 'libro', 'comentario', 'fecha']

class ReseñasEliminar(DeleteView):
	model = Reseñas
	template_name = "eliminar_reseña.html"#'EliminarReseñas'<id>
	success_url = reverse_lazy('ListaLibros')
