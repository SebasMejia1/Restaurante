from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
# Create your views here.

# TODO: TODAS LAS VISTAS SON FUNCINES DE PYTHON


def Home(request):
    return render(request, 'home.html')


def MenuPlatos(request):
    # Esta vista va a utilizar un form de django
    # Crear un objeto de la clas
    Formulario = FormularioPlatos()
    # Creamos un dicc para enviar el form al html
    data = {
        'formulario': Formulario
    }
    return render(request, 'menuplatos.html', data)


def Empleados(request):
    # Esta vista va a utilizar un form de django
    # Crear un objeto de la clas
    Formulario = FormularioEmpleados()
    # Creamos un dicc para enviar el form al html
    data = {
        'formulario': Formulario
    }
    return render(request, 'empleados.html', data)
