from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import loginForm, registroForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Empleados
from franquicias.models import Franquicias


def index(request):
    franquiciaList=Franquicias.objects.all()
    return render(request,'index.html',{"form":loginForm,"franquiciaList":franquiciaList})

def login(request):
    login=loginForm(request.POST or None)
    if login.is_valid():
        datos=login.cleaned_data
        username =datos.get("user_name")
        password =datos.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            franquicia=Franquicias.objects.get(Nombre="Cali")
            return HttpResponseRedirect('home')
        else:
            fail="Datos Incorrectos"
            return render(request,'index.html',{"form":login, "fail":fail})
    return render(request,'index.html',{"form":login})

@login_required(login_url='/unimonito')
def home(request):
    sesion=request.user
    print(sesion)
    return render(request,'home.html',{"username":sesion})

def registro(request):
    registro=registroForm(request.POST or None)
    if registro.is_valid():
        datos=registro.cleaned_data
        username =datos.get("empl_nombre")
        cedula =datos.get("empl_cedula")
        telefono =datos.get("empl_telefono")
        empl_salario =datos.get("empl_salario")
        empl_pasword =datos.get("empl_pasword")
        franquicia=Franquicias.objects.get(Nombre="Cali")

        djangoUser=User.objects.create_user(datos.get("empl_nombre"),
         email="", password=empl_pasword, 
         first_name=datos.get("empl_nombre"), 
         last_name=datos.get("empl_nombre"))
        djangoUser.save()

        empleado=Empleados(Nombre=djangoUser, Cedula=cedula, 
            Telefono=telefono,
            Salario=empl_salario,
            Empleado="empl_empleado",
            idFranquicia=franquicia)
        empleado.save()
        franquiciaList=Franquicias.objects.all()
        return render(request,'index.html',{"form":loginForm,"franquiciaList":franquiciaList})
    return render(request,'registro.html',{"form":registroForm})