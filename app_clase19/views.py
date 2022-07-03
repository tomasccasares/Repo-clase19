from django.shortcuts import render
from app_clase19.models import Productos, Estudiante

def listado_de_productos(request):

    datos = {}
    datos['productos'] = Productos.objects.all()

    return render(request, 'app_clase19/listado_de_productos.html', datos)

def listado_de_estudiantes(request):

    objetos = {}
    objetos['estudiantes'] = Estudiante.objects.all()

    return render(request, 'app_clase19/listado_de_estudiantes.html', objetos)



def a():
    pass
def b():
    pass
def g():
    pass



def mostrar_index(request):
    
    return render(request, 'app_clase19/index.html', {})










