from django import forms
from .models import Libro, Editoriales, Genero, Reseñas
from django.contrib.auth.models import User


class LibroFormulario(forms.Form):
	titulo= forms.CharField()
	autor= forms.CharField()
	genero= forms.ModelChoiceField(queryset=Genero.objects.all())
	publicacion = forms.IntegerField()
	sinopsis= forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 30}), required=False)
	class Meta:
		model = Libro
		fields = ['titulo', 'autor', 'genero', 'publicacion', 'sinopsis']

class AutorFormulario(forms.Form):
	nombre= forms.CharField()
	apellido= forms.CharField()
	nacionalidad= forms.CharField()

class EditorialFormulario(forms.Form):
	nombre= forms.CharField()
	pais= forms.CharField()
	direccion= forms.CharField()
	email=forms.EmailField()
	libros = forms.ModelChoiceField(queryset=Libro.objects.all(), required=False)
	class Meta:
		model = Editoriales
		fields = ['nombre', 'pais', 'direccion', 'libros']

class Reseñas(forms.Form):
    usuario = forms.ModelChoiceField(queryset=User.objects.all())
    libro = forms.ModelChoiceField(queryset=Libro.objects.all())
    comentario = forms.CharField()
    fecha = forms.DateField()
    class Meta:
        model = Reseñas
        fields = ['usuario', 'libro', 'comentario', 'fecha']
        unique_together = ['usuario', 'libro']
