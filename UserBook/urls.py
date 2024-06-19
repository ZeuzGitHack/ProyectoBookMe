from django.urls import path
from UserBook.views import *


urlpatterns = [
    path('login/', login_view, name="Login"),
    path('usuaro/', usuario_view, name="Usuario"),
    path('registro/', registro, name= "Registro"),
]
