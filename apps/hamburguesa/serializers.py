from rest_framework import serializers
from .models import  TipoIngrediente, Rol, Ingrediente, EstadoPedido, Pedido, DetallePedido

class TipoIngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIngrediente
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'
    
class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'


class EstadoPedidoSerializers(serializers.ModelSerializer):
    class Meta:
        model = EstadoPedido
        fields = '__all__'

class PedidoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class DetallePedidoSerializers(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = '__all__'

