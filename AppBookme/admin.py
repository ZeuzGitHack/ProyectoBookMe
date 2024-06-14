from django.contrib import admin
from AppBookme.models import Libro, Autores, Genero, Editoriales, Reseñas

# Register your models here.
admin.site.register(Libro)
admin.site.register(Autores)
admin.site.register(Genero)
admin.site.register(Editoriales)
admin.site.register(Reseñas)