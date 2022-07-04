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





def mostrar_index(request):

    #                                               aca esta el contexto con la variable y el valor
    return render(request, 'app_clase19/index.html', {'mi_titulo' : 'Hola! este es mi primer website :) '})










