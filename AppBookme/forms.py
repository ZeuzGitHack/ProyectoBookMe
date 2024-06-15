from django import forms
from .models import Libro
from django.contrib.auth.models import User


class LibroFormulario(forms.Form):
	titulo= forms.CharField()
	autor= forms.CharField()
	genero= forms.CharField()
	publicacion = forms.IntegerField()
	sinopsis= forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 30}), required=False)
	class Meta:
		model = Libro
		fields = ['campo_texto']

class AutorFormulario(forms.Form):
	nombre= forms.CharField()
	apellido= forms.CharField()
	nacionalidad= forms.CharField()

class EditorialFormulario(forms.Form):
	nombre= forms.CharField()
	pais= forms.CharField()
	direccion= forms.CharField()
	libros = forms.ForeignKey(Libro, on_delete=forms.CASCADE)

class Reseñas(forms.Form):
    usuario= forms.ForeignKey(User, on_delete=forms.CASCADE)
    libro = forms.ForeignKey(Libro, on_delete=forms.CASCADE, related_name='reseñas')
    comentario = forms.TextField()
    fecha = forms.DateTimeField()
    class Meta:
        unique_together = ['usuario', 'libro']
