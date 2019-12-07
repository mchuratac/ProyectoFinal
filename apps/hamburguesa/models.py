
from django.contrib.auth.models import User
import uuid
from django.db import models


# Create your models here.


class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=100, null = True , blank=True)
    status = models.CharField(max_length=100, null = True , blank=True)

    def __str__(self):
        return (self.rol)

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    age = models.IntegerField()
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return (self.user.username)

class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True)
    ingrediente = models.CharField(max_length=100, null = True , blank=True)
    precio = models.DecimalField(max_digits=16, decimal_places=2)
    cantidad = models.IntegerField(default=1)
    imagen = models.ImageField(upload_to="pictures", null=True)

    def __str__(self):
        return f'{str(self.ingrediente)}'

class TipoIngrediente(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100, null = True, blank=True)
    ingrediente = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return f'{str(self.tipo)}'

class EstadoPedido(models.Model):
    id = models.AutoField(primary_key=True)
    Estado = models.CharField(max_length=255, null = True, blank=True)

    def __str__(self):
        return (self.estado)

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=255, null = True, blank = True)
    fecha_pedido = models.DateTimeField()
    monto_total = models.DecimalField(max_digits=16, decimal_places=2)
    estado = models.ForeignKey(EstadoPedido, on_delete = models.CASCADE)
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return (self.id)

class DetallePedido(models.Model):
    id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete= models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete = models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio = models.DecimalField(max_digits=16, decimal_places=2)

    def __str__(self):
        return (self.ingrediente)

