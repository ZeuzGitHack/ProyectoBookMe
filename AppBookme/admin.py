from django.contrib import admin
from AppBookme.models import Libro, Autores, Genero, Editoriales, Reseñas, Avatar

class LibrosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor']

class GeneroAdmin(admin.ModelAdmin):
    list_display = ['nombre',]

class AutoresAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido']


# Register your models here.
admin.site.register(Libro, LibrosAdmin)
admin.site.register(Autores, AutoresAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Editoriales)
admin.site.register(Reseñas)
admin.site.register(Avatar)