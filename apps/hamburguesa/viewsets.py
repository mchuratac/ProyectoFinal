from rest_framework import viewsets,filters, permissions
from .serializers import  AuthSerializer,UsuarioSerializer,RolSerializer,TipoIngredienteSerializer,IngredienteSerializer, EstadoPedidoSerializer, PedidoSerializer, DetallePedidoSerializer
from django.contrib.auth.models import User
from .models import Usuario,Rol,TipoIngrediente, Ingrediente, EstadoPedido,Pedido, DetallePedido


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class RolViewSet(viewsets.ModelViewSet):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()

class AuthViewSet(viewsets.ModelViewSet):
    serializer_class = AuthSerializer
    queryset = User.objects.all()

class TipoIngredienteViewSet(viewsets.ModelViewSet):
    serializer_class = TipoIngredienteSerializer
    queryset = TipoIngrediente.objects.all()

class IngredienteViewSet(viewsets.ModelViewSet):
    serializer_class = IngredienteSerializer
    queryset = Ingrediente.objects.all()


class RolViewSet(viewsets.ModelViewSet):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()

class EstadoPedidoViewSet(viewsets.ModelViewSet):
    serializer_class = EstadoPedidoSerializer
    queryset = EstadoPedido.objects.all()

class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()

class DetallePedidoViewSet(viewsets.ModelViewSet):
    serializer_class = DetallePedidoSerializer
    queryset = DetallePedido.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('precio')
    
      
