from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.models import Platos
from web.models import Empleados
# Create your views here.

# TODO: TODAS LAS VISTAS SON FUNCINES DE PYTHON


def Home(request):
    return render(request, 'home.html')


def MenuPlatos(request):
    # RUTINA PARA CONSULTA DE PLATOS
    platosConsultados = Platos.objects.all()
    print(platosConsultados)

    # RUTINA PARA GUARDAR PLATS
    # Esta vista va a utilizar un form de django
    # Crear un objeto de la clas
    Formulario = FormularioPlatos()
    # Creamos un dicc para enviar el form al html
    data = {
        'formulario': Formulario,
        'bandera': False,
        'platos': platosConsultados
    }

    # RECIBIR DATOS DEL FORM
    if (request.method == "POST"):
        datosForm = FormularioPlatos(request.POST)
        # print(datosForm)
        if (datosForm.is_valid()):
            datosLimpios = datosForm.cleaned_data
            # print(datosLimpios)
            # CONSTRUIR UN DICC DE ENVIO DE DATOS A LA DB
            platoNuevo = Platos(
                nombre=datosLimpios["nombre"],
                descripcion=datosLimpios["descripcion"],
                imagen=datosLimpios["fotografia"],
                precio=datosLimpios["precio"],
                tipo=datosLimpios["tipo"]
            )
            # INTENTARË LLEVAR DAOS A LA DB
            try:
                platoNuevo.save()
                data["bandera"] = True
                print("EXITO GUARDANDO DATOS")
            except Exception as error:
                print("Upss...", error)
                data["bandera"] = False
    return render(request, 'menuplatos.html', data)


def EmpleadosClas(request):
    # Esta vista va a utilizar un form de django
    # Crear un objeto de la clas
    Formulario = FormularioEmpleados()
    # Creamos un dicc para enviar el form al html
    data = {
        'formulario': Formulario,
        'bandera': False
    }
    if (request.method == "POST"):
        datosEmpleados = FormularioEmpleados(request.POST)
        if (datosEmpleados.is_valid()):
            datosLimpiosEmpleados = datosEmpleados.cleaned_data
            # print(datosLimpiosEmpleados)
            # CONSTRUIR UN DICC DE ENVIO DE DATOS A LA DB
            empleadoNuevo = Empleados(
                nombre=datosLimpiosEmpleados["nombre"],
                apellidos=datosLimpiosEmpleados["apellidos"],
                foto=datosLimpiosEmpleados["foto"],
                cargo=datosLimpiosEmpleados["cargo"],
                salario=datosLimpiosEmpleados["salario"],
                contacto=datosLimpiosEmpleados["contacto"]
            )
            # INTENTARË LLEVAR DAOS A LA DB
            try:
                empleadoNuevo.save()
                print("EXITO GUARDANDO DATOS")
                data["bandera"] = True
            except Exception as error:
                data["bandera"] = False
                print("Upss...", error)
    return render(request, 'empleados.html', data)
