from rest_framework import viewsets,filters
from .serializers import TipoIngredienteSerializer,IngredienteSerializer,  RolSerializer, EstadoPedidoSerializer, PedidoSerializer, DetallePedidoSerializer
from .models import TipoIngrediente, Ingrediente,Rol, EstadoPedido,Pedido, DetallePedido

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
    
      
