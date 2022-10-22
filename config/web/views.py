from django.shortcuts import render

# Create your views here.

# TODO: TODAS LAS VISTAS SON FUNCINES DE PYTHON

def Home(request):
    return render(request,'home.html')
