from django import forms
from .models import Libro, Editoriales, Genero, Reseñas, Avatar
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


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

class ReseñasForm(forms.ModelForm):
	class Meta:
		model = Reseñas
		fields=['comentario', 'calificacion']


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
	password = forms.CharField(
    help_text="",
    widget=forms.HiddenInput(), required=False)
	password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
	class Meta:
		model=User
		fields = ["username", "first_name", "last_name", "email"]
	def clean_password2(self):
		password1 = self.cleaned_data["password1"]
		password2 = self.cleaned_data["password2"]
		if password1 != password2:
			raise forms.ValidationError("Las contraseñas deben ser iguales")
		return password2

class AvatarFormulario(forms.ModelForm):

  class Meta:
    model=Avatar
    fields=('imagen',)