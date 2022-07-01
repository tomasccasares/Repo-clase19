from django.db import models

class Productos(models.Model):
    
    producto = models.CharField(max_length = 40)

    cantidad = models.IntegerField()
