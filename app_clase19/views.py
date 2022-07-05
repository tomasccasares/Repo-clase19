from django.shortcuts import render
from app_clase19.models import (Productos,
    Estudiante, Profesor, Curso
 )

def dataProductos(request):

    datos = {}
    datos['productos'] = Productos.objects.all()

    return render(request, 'app_clase19/data_productos.html', datos)

def dataEstudiante(request):

    objetos = {}
    objetos['estudiantes'] = Estudiante.objects.all()

    return render(request, 'app_clase19/data_estudiantes.html', objetos)

def mostrarIndex(request):

    #                                               aca esta el contexto con la variable y el valor
    return render(request, 'app_clase19/index.html', {'mi_titulo' : 'Hola! este es mi primer website :) '})

def dataCurso(request):
    
    contextoCurso = {}
    contextoCurso['curso'] = Curso.objects.all()
    return render(request, 'app_clase19/data_curso.html', contextoCurso)

def dataProfesor(request):
    
    contextoProfesor = {}
    contextoProfesor['profesor'] = Profesor.objects.all()
    return render(request, 'app_clase19/data_profesor.html', contextoProfesor)


















