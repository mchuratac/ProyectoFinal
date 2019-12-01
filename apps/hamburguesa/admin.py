
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TipoIngrediente ,Rol ,Ingrediente ,EstadoPedido, Pedido, DetallePedido

# Register your models here.

admin.site.register(TipoIngrediente)
admin.site.register(Rol)
admin.site.register(Ingrediente)
admin.site.register(EstadoPedido)
admin.site.register(Pedido)
admin.site.register(DetallePedido)


