from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.categoria




class Producto(models.Model):
     nombre = models.CharField(max_length=200)
     precio = models.IntegerField()
     stock = models.IntegerField()
     descripcion = models.CharField(max_length=200)
     categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
     imagen = models.ImageField(null=True,blank=True)
     vigente = models.BooleanField()
     

     def __str__(self):
      return self.nombre


class Empleado(models.Model):
    nombreEmp = models.CharField(max_length=100)
    edad = models.IntegerField()
    rut = models.CharField(max_length=11)
    direccion = models.CharField(max_length=100) 
    correo = models.CharField(max_length=100) 

    def __str__(self):
      return self.nombreEmp

    
class Cliente(models.Model):
    nombreCli = models.CharField(max_length=100)
    edad = models.IntegerField()
    rut = models.CharField(max_length=11)
    direccion = models.CharField(max_length=100) 
    correo = models.CharField(max_length=100) 

    def __str__(self):
      return self.nombreCli
