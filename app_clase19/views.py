from django.shortcuts import render
from app_clase19.models import Productos

def listado_de_productos(request):

    datos = {}
    datos['productos'] = Productos.objects.all()

    return render(request, 'app_clase19/index.html', datos)

