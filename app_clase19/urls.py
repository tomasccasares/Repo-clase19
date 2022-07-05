from django.contrib import admin
from django.urls import path
from app_clase19.views import (
    dataProfesor, dataCurso,
    dataEstudiante, dataProductos,
    mostrarIndex,
)


urlpatterns = [
    path('data-de-productos-BBI/', dataProductos),
    path('data-estudiante/', dataEstudiante),
    path('index-html/', mostrarIndex),
    path('data-curso/', dataCurso),
    path('data-profesor/', dataProfesor),
] 
