from django.urls import path
from UserBook.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', login_view, name="Login"),
    path('usuaro/', usuario_view, name="Usuario"),
    path('registro/', registro, name= "Registro"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('editar-usuario/', editar_usuario, name="EditarUsuario"),
]
