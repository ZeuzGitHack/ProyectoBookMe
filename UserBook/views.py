from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from AppBookme.forms import UserRegisterForm, UserEditForm, AvatarFormulario
from AppBookme.models import Avatar
from django.contrib.auth.mixins import LoginRequiredMixin
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
            data = miFormulario.cleaned_data
            usuario = data["username"]
            miFormulario.save()
            return render(req, "usuario.html", {"username":usuario, "mensaje":f"Usuario '{usuario}' creado con exito"})
        else:
            return render(req, "registro.html", {"mensaje":"Datos invalidas"})
    else:
        miFormulario = UserRegisterForm()
        return render(req, "registro.html", {"miFirmulario":miFormulario})

@login_required
def editar_usuario(req):
  usuario = req.user
  if req.method == 'POST':
    formUsuario = UserEditForm(req.POST, instance=req.user)
    if formUsuario.is_valid():
      data = formUsuario.cleaned_data
      usuario.username = data["username"]
      usuario.first_name = data["first_name"]
      usuario.last_name = data["last_name"]
      usuario.email = data["email"]
      usuario.set_password(data["password1"])
      usuario.save()
      return render(req, "usuario.html", {
            "mensaje2": "Datos actualizados con éxito",
            'username': usuario.username,
            'email': usuario.email,
            'nombre': usuario.first_name,
            'apellido': usuario.last_name})
    else:
      formUsuario = UserEditForm(instance=req.user)
      return render(req, "editar_usuario.html", {"mensaje" : "Datos erroneos, intente nuevamente","formUsuario": formUsuario})
  else:
    formUsuario = UserEditForm(instance=req.user)
    return render(req, "editar_usuario.html", {"formUsuario": formUsuario})

@login_required
def agregar_avatar(req):
  usuario = req.user
  if req.method == 'POST':
    avatarForm = AvatarFormulario(req.POST, req.FILES)
    if avatarForm.is_valid():
      data = avatarForm.cleaned_data
      avatar = Avatar(user=req.user, imagen=data["imagen"])
      avatar.save()
      return render(req, "usuario.html", {"mensaje": "Avatar cargado con éxito",'username': usuario.username, 'email': usuario.email, 'nombre': usuario.first_name, 'apellido': usuario.last_name})    
    else:
      return render(req, "inicio.html", {"mensaje": "Datos inválidos"}) 
  else:
    avatarForm = AvatarFormulario()
    return render(req, "agregar_avatar.html", {"avatarForm": avatarForm})

@login_required
def cambiar_avatar(req):
    usuario = req.user
    if req.method == 'POST':
        formAvatar = AvatarFormulario(req.POST, req.FILES)
        if formAvatar.is_valid():
            data = formAvatar.cleaned_data
            user = req.user
            avatar = Avatar.objects.filter(user=user).first()
            if avatar:
                avatar.imagen = data["imagen"]
            else:
                avatar = Avatar(user=user, imagen=data["imagen"])
            avatar.save()
            return render(req, "usuario.html", {"mensaje": "Avatar modificado con éxito",'username': usuario.username, 'email': usuario.email, 'nombre': usuario.first_name, 'apellido': usuario.last_name})
        else:
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    else:
        formAvatar = AvatarFormulario()
        return render(req, "cambiar_avatar.html", {"formAvatar": formAvatar})
