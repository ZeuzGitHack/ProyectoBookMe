from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from AppBookme.models import Autores, Genero, Libro, Editoriales, Reseñas
from .forms import LibroFormulario, AutorFormulario, ReseñasForm, EditorialFormulario
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
	ordering="titulo"

class LibrosDetalles(DetailView):
	model = Libro
	template_name = "detalle_libro.html"
	context_object_name = "libro"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['reseñas'] = Reseñas.objects.filter(libro=self.object)
		return context

@login_required
def libroFormulario(req):
	libros=Libro.objects.all()

	if req.method == 'POST':
		miFormulario = LibroFormulario(req.POST)
		if miFormulario.is_valid():
			data = miFormulario.cleaned_data
			nuevo_libro = Libro(titulo=data['titulo'], autor=data['autor'], genero=data['genero'], publicacion=data['publicacion'], sinopsis=data['sinopsis'])
			nuevo_libro.save()
			return render(req, "lista_libros.html", {"mensaje": "Nuevo libro guardado con exito", "libros":libros})
		else:
			return render(req, "lista_libros.html", {"mensaje2": "Datos inválidos", "libros":libros})
	else:
		miFormulario = LibroFormulario()
		return render(req, "formulario_libro.html", {"miFormulario": miFormulario})

@login_required
@staff_member_required(login_url='/UserBook/usuaro/')
def editar_libro(req, id):
  libros=Libro.objects.all()
  if req.method == 'POST':
    libroForm = LibroFormulario(req.POST)
    if libroForm.is_valid():
      data = libroForm.cleaned_data
      libro = Libro.objects.get(id=id)
      libro.titulo = data["titulo"]
      libro.autor = data["autor"]
      libro.genero = data["genero"]
      libro.publicacion = data["publicacion"]
      libro.sinopsis = data["sinopsis"]
      libro.save()
      return render(req, "lista_libros.html", {"mensaje": "libro actualizado con éxito", "libros":libros})
    else:
      return render(req, "lista_libros.html", {"mensaje": "Datos inválidos", "libros":libros})
  else:
    libro = Libro.objects.get(id=id)

    libroForm = LibroFormulario(initial={
      "titulo": libro.titulo,
      "autor": libro.autor,
      "genero": libro.genero,
      "publicacion": libro.publicacion,
      "sinopsis": libro.sinopsis,
    })

    return render(req, "editar_libro.html", {"libroForm": libroForm, "id": libro.id})

@login_required
@staff_member_required(login_url='/UserBook/usuaro/')
def eliminar_libro(req, id):
  libros = Libro.objects.all()
  if req.method == 'POST':
    libro = Libro.objects.get(id=id)
    libro.delete()
  return render(req, "lista_libros.html", {"libros": libros})

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
	context_object_name = "autores"

class AutoresDetalles(DetailView):
	model = Autores
	template_name = "detalle_autores.html"
	context_object_name = "autor"

@login_required
def autorFormulario(req):
	autores=Autores.objects.all()
	if req.method == 'POST':
		miFormulario = AutorFormulario(req.POST)
		if miFormulario.is_valid():
			miFormulario.save()
			return render(req, "lista_autores.html", {"mensaje": "Nuevo autor guardado con exito", "autores":autores})
		else:
			return render(req, "lista_autores.html", {"mensaje2": "Datos inválidos"})
	else:
		miFormulario = AutorFormulario()
		return render(req, "formulario_autores.html", {"miFormulario": miFormulario})

@login_required
@staff_member_required(login_url='/UserBook/usuaro/')
def editar_autor(req, id):
  autores=Autores.objects.all()
  if req.method == 'POST':
    autorForm = AutorFormulario(req.POST)
    if autorForm.is_valid():
      data = autorForm.cleaned_data
      autor = Autores.objects.get(id=id)
      autor.nombre = data["nombre"]
      autor.apellido = data["apellido"]
      autor.nacionalidad = data["nacionalidad"]
      autor.save()
      return render(req, "lista_autores.html", {"mensaje": "Autor actualizado con éxito", "autores":autores})
    else:
      return render(req, "lista_autores.html", {"mensaje2": "Datos inválidos", "autores":autores})
  else:
    autor = Autores.objects.get(id=id)

    autorForm = AutorFormulario(initial={
      "nombre": autor.nombre,
      "apellido": autor.apellido,
      "nacionalidad": autor.nacionalidad,
    })

    return render(req, "editar_autores.html", {"autorForm": autorForm, "id": autor.id})

@login_required
@staff_member_required(login_url='/UserBook/usuaro/')
def eliminar_autor(req, id):
  autores = Autores.objects.all()
  if req.method == 'POST':
    autor = Autores.objects.get(id=id)
    autor.delete()
  return render(req, "lista_autores.html", {"autores": autores})

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
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['libros'] = self.object.libros.all()
		return context

#Editoriales

class EditorialesLista(ListView):
	model = Editoriales
	template_name = "lista_editoriales.html"
	context_object_name = "editoriales"

class EditorialesDetalles(DetailView):
	model = Editoriales
	template_name = "detalle_editoriales.html"
	context_object_name = "editorial"

@login_required
@staff_member_required(login_url='/UserBook/usuaro/')
def editar_editorial(req, id):
  editoriales=Editoriales.objects.all()
  if req.method == 'POST':
    editForm = EditorialFormulario(req.POST)
    if editForm.is_valid():
      data = editForm.cleaned_data
      editorial = Editoriales.objects.get(id=id)
      editorial.nombre = data["nombre"]
      editorial.pais = data["pais"]
      editorial.direccion = data["direccion"]
      editorial.contacto = data["contacto"]
      editorial.libros = data["libros"]
      editorial.save()
      return render(req, "lista_editoriales.html", {"mensaje": "Autor actualizado con éxito", "editoriales":editoriales})
    else:
      return render(req, "lista_editoriales.html", {"mensaje2": "Datos inválidos", "editoriales":editoriales})
  else:
    editorial = Editoriales.objects.get(id=id)

    editForm = EditorialFormulario(initial={
      "nombre": editorial.nombre,
      "pais": editorial.pais,
      "direccion": editorial.direccion,
      "contacto": editorial.contacto,
      "libros": editorial.libros,
    })

    return render(req, "editar_editorial.html", {"editForm": editForm, "id": editorial.id})

@login_required
@staff_member_required(login_url='/UserBook/usuaro/')
def eliminar_editorial(req, id):
  editoriales = Editoriales.objects.all()
  if req.method == 'POST':
    editorial = Editoriales.objects.get(id=id)
    editorial.delete()
  return render(req, "lista_editoriales.html", {"editoriales": editoriales})

#Reseñas
@login_required
def reseña_libro(req, libro_id):
	libros=Libro.objects.all()
	try:
		libro=Libro.objects.get(id=libro_id)
	except libro.DoesNotExist:
		render(req, "inicio.html, {}")
	try:
		if req.method == 'POST':
			formResena = ReseñasForm(req.POST)
			if formResena.is_valid():
				reseña = formResena.save(commit=False)
				reseña.libro = libro
				reseña.usuario = req.user
				reseña.save()
				return render(req, "lista_libros.html", {"libro":libro})
		else:
			formResena = ReseñasForm()
			return render(req, "reseña.html", {"formResena":formResena, "libro":libro})
	except:
		return render(req, "lista_libros.html", {"mensaje": "Solo se puede realizar un comentario por libro","libros":libros})

