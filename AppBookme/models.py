from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Autores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    nacionalidad= models.CharField(max_length=25)
    
    def __str__(self):
        return f"{self.nombre}-{self.apellido}-{self.nacionalidad}"

class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre}/n{self.descripcion}"

class Libro(models.Model):
    titulo = models.CharField(max_length=40, unique=True)
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE, related_name='libros')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='libros')
    publicacion = models.IntegerField()
    sinopsis= models.TextField(default="Sin sinopsis")

    def __str__(self):
        return f"{self.titulo}-{self.autor}-{self.genero}-{self.publicacion}"

class Editoriales(models.Model):
    nombre = models.CharField(max_length=40)
    pais= models.CharField(max_length=40)
    direccion = models.CharField(max_length=50)
    libros = models.ForeignKey(Libro, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre}-{self.pais}-{self.direccion}"

class Reseñas(models.Model):
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='reseñas')
    comentario = models.TextField()
    fecha = models.DateTimeField()

    class Meta:
        unique_together = ['usuario', 'libro']

# class ListaDeseos(models.Model):

# class EstanteriaVirtual(models.Model):

# class VentaIntercambio(models.Model):



