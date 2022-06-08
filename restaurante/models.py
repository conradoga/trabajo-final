from django.db import models

# Create your models here.
class hamburguesas(models.Model):
    nombre = models.CharField(max_length= 30)
    ingredientes = models.CharField(max_length= 15)
    descripcion = models.CharField(max_length= 40)
    precio = models.IntegerField(max_length= 5)
class ensaladas(models.Model):
    nombre = models.CharField(max_length= 30)
    ingredientes = models.CharField(max_length= 15)
    descripcion = models.CharField(max_length= 40)
    precio = models.IntegerField(max_length= 5)
class bebidas(models.Model):
    nombre = models.CharField(max_length= 30)
    descripcion = models.CharField(max_length= 40)
    precio = models.IntegerField(max_length= 5)


