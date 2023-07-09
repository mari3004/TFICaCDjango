from django.db import models

# Create your models here.

class Clientes(models.Model): 
    legajo=models.IntegerField()
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30) 
    direccion=models.CharField(max_length=50) 
    email=models.EmailField() 
    telefono=models.CharField(max_length=7) 
    
class Articulos(models.Model): 
    codigo=models.CharField(max_length=7)
    nombre=models.CharField(max_length=30) 
    seccion=models.CharField(max_length=20) 
    precio=models.IntegerField() 
    
class Pedidos(models.Model): 
    numero=models.IntegerField() 
    fecha=models.DateField() 
    entregado=models.BooleanField()