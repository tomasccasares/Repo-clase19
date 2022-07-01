from django.db import models

class Productos(models.Model):
    
    producto = models.CharField(max_length = 40)

    cantidad = models.IntegerField()

# al instanciar la clase y crear objetos nuevos, esos objetos donde almaceno la instanciacion, pasan a ser
# objetos de tipo: class, en este caso de tipo: Productos
# entonces en el template, en: {% for elemento in productos %}
# la variable de control: elemento, por cada elemento(objeto) que tome dentro de la lista de objetos que se encuentra
# comovalor de la clave: productos, sera tambien un objeto de tipo: class tambien
