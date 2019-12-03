from django.urls import path
from .views import TipoIngredienteApiList, IngredienteApiList , RolApiList, EstadoPedidoApiList,PedidoApiList, DetallePedidoApiList 

urlpatterns = [
    path('list_tipoingrediente/', TipoIngredienteApiList.as_view()),
    path('list_ingrediente/', IngredienteApiList.as_view()),
    path('list_rol/', RolApiList.as_view()),
    path('list_estadopedido/', EstadoPedidoApiList.as_view()),
    path('list_pedido/', PedidoApiList.as_view()),
    path('list_detallepedido/', DetallePedidoApiList.as_view()),
]

