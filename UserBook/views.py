from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from AppBookme.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required


def login_view(req):
    if req.method == 'POST':
        miFormulario = AuthenticationForm(req, data=req.POST)
    
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            usuario=data["username"]
            psw = data["password"]
            user=authenticate(username=usuario, password=psw)
            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje":f"{usuario}"})
            else:
                return render(req, "inicio.html", {"mensaje":"Credenciales invalidas"})
        else:
            return render(req, "inicio.html", {"mensaje":"Credenciales invalidas"})
    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFirmulario":miFormulario})

@login_required
def usuario_view(req):
    if req.user.is_authenticated:
        user = req.user
        return render(req, "usuario.html", {'username': user.username,'email': user.email, 'nombre':user.first_name, 'apellido':user.last_name})
    else:
        return req("login.html", {})

def registro(req):
    if req.method == 'POST':
        miFormulario = UserRegisterForm(req.POST)
        if miFormulario.is_valid():
            username=miFormulario.cleaned_data
            miFormulario.save()
            return render(req, "usuario.html", {"username":username, "mensaje":f"Usuario {username} creado con exito"})
        else:
            return render(req, "registro.html", {"mensaje":"Datos invalidas"})
    else:
        miFormulario = UserRegisterForm()
        return render(req, "registro.html", {"miFirmulario":miFormulario})

@login_required
def editar_usuario(req):
    usuario = req.user
    if req.method == 'POST':
        miFormulario = UserEditForm(req.POST, instance=req.user)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()
            return render(req, "usuario.html", {"mensaje2": "Datos actualizado con éxito"})
        else:
            return render(req, "editar_usuario.html", {"miFormulario": miFormulario})
    else:
        miFormulario = UserEditForm(instance=req.user)
        return render(req, "editar_usuario.html", {"miFormulario": miFormulario})