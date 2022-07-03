from django.contrib import admin
from django.urls import path
from app_clase19.views import (listado_de_productos,
     listado_de_estudiantes, mostrar_index )


urlpatterns = [
    path('listado-de-productos-BBI/', listado_de_productos),
    path('listado-de-estudiantes/', listado_de_estudiantes),
    path('index-html/', mostrar_index)
] 