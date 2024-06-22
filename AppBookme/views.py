from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from AppBookme.models import Autores, Genero, Libro, Editoriales, Reseñas
from .forms import LibroFormulario, AutorFormulario, EditorialFormulario, Reseñas
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required

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

@login_required
@staff_member_required(login_url="/AppBookme/")
def libroFormulario(req):

	if req.method == 'POST':
		miFormulario = LibroFormulario(req.POST)
		if miFormulario.is_valid():
			data = miFormulario.cleaned_data
			nuevo_libro = Libro(titulo=data['titulo'], autor=data['autor'], genero=data['genero'], publicacion=data['publicacion'], sinopsis=data['sinopsis'])
			nuevo_libro.save()
			return render(req, "inicio.html", {"message": "Nuevo libro guardado con exito"})
		else:
			return render(req, "inicio.html", {"message": "Datos inválidos"})
	else:
		miFormulario = LibroFormulario()
		return render(req, "formulario_libro.html", {"miFormulario": miFormulario})

class LibroEditar(LoginRequiredMixin, UpdateView):
	model = Libro
	template_name = "editar_libro.html"
	success_url = reverse_lazy('ListaLibros')
	fields = ['titulo', 'autor', 'genero', 'publicacion', 'sinopsis']

class LibroEliminar(LoginRequiredMixin, DeleteView):
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

@login_required
@staff_member_required(login_url="/AppBookme/")
def autorFormulario(req):

	if req.method == 'POST':
		miFormulario = AutorFormulario(req.POST)
		if miFormulario.is_valid():
			data = miFormulario.cleaned_data
			nuevo_autor = Autores(nombre=data['nombre'], apellido=data['apellido'], nacionalidad=data['nacionalidad'])
			nuevo_autor.save()
			return render(req, "inicio.html", {"message": "Nuevo autor guardado con exito"})
		else:
			return render(req, "inicio.html", {"message": "Datos inválidos"})
	else:
		miFormulario = AutorFormulario()
		return render(req, "formulario_autores.html", {"miFormulario": miFormulario})

class AutoresEditar(LoginRequiredMixin, UpdateView):
	model = Autores
	template_name = "editar_autores.html"
	success_url = reverse_lazy('ListaAutores')
	fields = ['nombre', 'apellido', 'nacionalidad']
	context_object_name = "autor"

class AutoresEliminar(LoginRequiredMixin, DeleteView):
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

class GenerosEditar(LoginRequiredMixin, UpdateView):
	model = Genero
	template_name = "editar_genero.html"
	success_url = reverse_lazy('ListaGeneros')
	fields = ['nombre', 'descripcion']

class GenerosEliminar(LoginRequiredMixin, DeleteView):
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

class EditorialesEditar(LoginRequiredMixin, UpdateView):
	model = Editoriales
	template_name = "editar_editorial.html"
	success_url = reverse_lazy('ListaEditoriales')
	fields = ['nombre', 'pais', 'direccion', 'libros']

class EditorialesEliminar(LoginRequiredMixin, DeleteView):
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
