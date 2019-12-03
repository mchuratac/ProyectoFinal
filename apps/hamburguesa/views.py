from django.shortcuts import render
from rest_framework import generics
from .serializers import TipoIngredienteSerializer, IngredienteSerializer, RolSerializer, PedidoSerializer, DetallePedidoSerializer, EstadoPedidoSerializer
from .models import TipoIngrediente, Ingrediente, Rol, Pedido, DetallePedido, EstadoPedido

# Create your views here.

class TipoIngredienteApiList(generics.ListAPIView):
    queryset = TipoIngrediente.objects.all()
    serializer_class = TipoIngredienteSerializer

class IngredienteApiList(generics.ListAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

class RolApiList(generics.ListAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = RolSerializer

class EstadoPedidoApiList(generics.ListAPIView):
    queryset = EstadoPedido.objects.all()
    serializer_class = EstadoPedidoSerializer

class PedidoApiList(generics.ListAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class DetallePedidoApiList(generics.ListAPIView):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer

