
from django.contrib.auth.models import User
import uuid
from django.db import models

# Create your models here.
class TipoIngrediente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100, null = True, blank=True)

    def __str__(self):
        return f'{str(self.nombre)}'


class Rol(models.Model):
    id = models.UUIDField (primary_key=True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length=100, null = True , blank=True)
    status = models.CharField(max_length=100, null = True , blank=True)

class Ingrediente(models.Model):
    id = models.UUIDField (primary_key=True, default= uuid.uuid4, editable = False)
    nombre = models.CharField(max_length=100, null = True , blank=True)
    tipo = models.ForeignKey (TipoIngrediente,on_delete= models.CASCADE)
    precio = models.DecimalField(max_digits=16, decimal_places=4)
    cantidad = models.CharField(max_length=100, null = True , blank=True)
    #imagen = models.ImageField()


    def __str__(self):
        return f'{str(self.nombre)}'

class EstadoPedido(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable = False)
    nombre = models.CharField(max_length=255, null = True, blank=True)

class Pedido(models.Model):
    id = models.UUIDField (primary_key=True, default= uuid.uuid4, editable= False )
    fecha_pedido = models.DateTimeField()
    monto_total = models.DecimalField(max_digits=16, decimal_places=4)
    estado = models.ForeignKey(EstadoPedido, on_delete = models.CASCADE)
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)

class DetallePedido(models.Model):
    id = models.UUIDField (primary_key=True, default=uuid.uuid4, editable = False )
    pedido = models.ForeignKey(Pedido, on_delete= models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete = models.CASCADE)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=16, decimal_places=4)



