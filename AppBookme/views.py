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
    return render(req, "acerca_de_mi.html", {})# "AcercaDeMi"

class LibrosLista(ListView):
	model = Libro
	template_name = "lista_libros.html"# "ListaLibros"
	context_object_name = "libros"

class LibrosDetalles(DetailView):
	model = Libro
	template_name = "detalle_libro.html"#"DetalleLibro" <id>
	context_object_name = "libro"

class LibroFormulario(CreateView):
	model = Libro
	template_name = "formulario_libro.html"#'FormularioLibro'
	success_url = reverse_lazy('ListaLibros')
	fields = ['titulo', 'autor', 'genero', 'publicacion', 'sinopsis']

class LibroEditar(UpdateView):
	model = Libro
	template_name = "editar_libro.html"#'EditarLibro'<id>
	success_url = reverse_lazy('ListaLibros')
	fields = ['titulo', 'autor', 'genero', 'publicacion', 'reseña']

class LibroEliminar(DeleteView):
	model = Libro
	template_name = "eliminar_libro.html"#'EliminarLibro'<id>
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
	template_name = "detalle_autores.html"#'DetalleAutores'<id>
	context_object_name = "autor"

class AutoresFormulario(CreateView):
	model = Autores
	template_name = "formulario_autores.html"#'FormularioAutores'
	success_url = reverse_lazy('ListaAutores')
	fields = ['nombre', 'apellido', 'nacionalidad']

class AutoresEditar(UpdateView):
	model = Autores
	template_name = "editar_autores.html"#'EditarAutores'<id>
	success_url = reverse_lazy('ListaAutores')
	fields = ['nombre', 'apellido', 'nacionalidad']

class AutoresEliminar(DeleteView):
	model = Autores
	template_name = "eliminar_autor.html"#'EliminarAutores'<id>
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

class GenerosLista(ListView):
	model = Genero
	template_name = "lista_genero.html"#'ListaGeneros'
	context_object_name = "genero"

class GenerosDetalles(DetailView):
	model = Genero
	template_name = "detalle_genero.html"#'DetalleGenero'<id>
	context_object_name = "genero"

class GeneroFormulario(CreateView):
	model = Genero
	template_name = "crear_genero.html"#'CrearGenero'
	success_url = reverse_lazy('ListaGeneros')
	fields = ['nombre', 'descripcion']

class GeneroEditar(UpdateView):
	model = Genero
	template_name = "editar_genero.html"#'EditarGenero'<id>
	success_url = reverse_lazy('ListaGeneros')
	fields = ['nombre', 'descripcion']

class GeneroEliminar(DeleteView):
	model = Genero
	template_name = "eliminar_genero.html"#'EliminarGenero'<id>
	success_url = reverse_lazy('ListaGeneros')

#Editoriales

class EditorialesLista(ListView):
	model = Editoriales
	template_name = "lista_Editoriales.html"#'ListaEditoriales'
	context_object_name = "editorial"

class EditorialesDetalles(DetailView):
	model = Editoriales
	template_name = "detalle_editoriales.html"#'DetalleEditoriales'<id>
	context_object_name = "editorial"

class EditorialesFormulario(CreateView):
	model = Editoriales
	template_name = "crear_editorial.html"#'CrearEditorial'
	success_url = reverse_lazy('ListaEditoriales')
	fields = ['nombre', 'pais', 'direccion', 'libros']

class EditorialesEditar(UpdateView):
	model = Editoriales
	template_name = "editar_editorial.html"#'EditarEditoriales'<id>
	success_url = reverse_lazy('ListaEditoriales')
	fields = ['nombre', 'pais', 'direccion', 'libros']

class EditorialesEliminar(DeleteView):
	model = Editoriales
	template_name = "eliminar_genero.html"#'EliminarEditoriales'<id>
	success_url = reverse_lazy('ListaEditoriales')

#Reseñas

class ReseñasFormulario(CreateView):
	model = Reseñas
	template_name = "crear_reseña.html"#'CrearReseña'
	success_url = reverse_lazy('ListaLibros')
	fields = ['usuario', 'libro', 'comentario', 'fecha']

class ReseñasEditar(UpdateView):
	model = Reseñas
	template_name = "editar_editorial.html"#'EditarReseñas'<id>
	success_url = reverse_lazy('ListaLibros')
	fields = ['usuario', 'libro', 'comentario', 'fecha']

class ReseñasEliminar(DeleteView):
	model = Reseñas
	template_name = "eliminar_reseña.html"#'EliminarReseñas'<id>
	success_url = reverse_lazy('ListaLibros')
