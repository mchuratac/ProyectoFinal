from rest_framework import serializers
from .models import  Usuario, Rol, User, TipoIngrediente,  Ingrediente, EstadoPedido, Pedido, DetallePedido
from django.contrib.auth.models import User


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password', 'first_name']
    
class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'

class TipoIngredienteSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = TipoIngrediente
        fields = ['id','tipo']


class EstadoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPedido
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = '__all__'

