from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


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

def usuario_view(req):
    if req.user.is_authenticated:
        user = req.user
        return render(req, "usuario.html", {'username': user.username,'email': user.email})
    else:
        return req("login.html", {})

def registro(req):
    if req.method == 'POST':
        miFormulario = UserCreationForm(req, data=req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            usuario=data["username"]
            miFormulario.save()
            return render(req, "usuario.html", {"username":usuario, "mensaje":f"Usuario {usuario} creado con exito"})
        else:
            return render(req, "registro.html", {"mensaje":"Datos invalidas"})
    else:
        miFormulario = UserCreationForm()
        return render(req, "registro.html", {"miFirmulario":miFormulario})