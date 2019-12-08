from django.urls import path,include

from .viewsets import  UsuarioViewSet,RolViewSet 
from .viewsets import TipoIngredienteViewSet, IngredienteViewSet
from .viewsets import EstadoPedidoViewSet, PedidoViewSet, DetallePedidoViewSet
from rest_framework import routers


#from .views import TipoIngredienteApiList, IngredienteApiList , RolApiList, EstadoPedidoApiList,PedidoApiList, DetallePedidoApiList 
'''
urlpatterns = [
    path('list_tipoingrediente/', TipoIngredienteApiList.as_view()),
    path('list_ingrediente/', IngredienteApiList.as_view()),
    path('list_rol/', RolApiList.as_view()),
    path('list_estadopedido/', EstadoPedidoApiList.as_view()),
    path('list_pedido/', PedidoApiList.as_view()),
    path('list_detallepedido/', DetallePedidoApiList.as_view()),
]
'''

router = routers.DefaultRouter()
router.register(r'Usuarios', UsuarioViewSet)
router.register(r'Rols', RolViewSet)
router.register(r'Ingredientes', IngredienteViewSet)
router.register(r'TipoIngredientes', TipoIngredienteViewSet)


router.register(r'EstadoPedidos', EstadoPedidoViewSet)
router.register(r'Pedidos', PedidoViewSet)
router.register(r'DetallePedidos', DetallePedidoViewSet)


urlpatterns = [
    path('hamburguesa/', include (router.urls))

]
