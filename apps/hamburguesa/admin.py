
from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Rol, Ingrediente, TipoIngrediente, EstadoPedido, Pedido, DetallePedido

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id','user','location','age','rol']

class RolAdmin(admin.ModelAdmin):
    list_display = ['id','rol','status']
    
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ['id','ingrediente','precio','cantidad','imagen']

class TipoIngredienteAdmin(admin.ModelAdmin):
    list_display=['id','tipo']

class EstadoPedidoAdmin(admin.ModelAdmin):
    list_display = ['id','estado']

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id','cliente','fecha_pedido','monto_total','estado','atendidopor']

class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ['id','pedido','ingrediente','cantidad','precio']

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(TipoIngrediente, TipoIngredienteAdmin)
admin.site.register(EstadoPedido, EstadoPedidoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(DetallePedido, DetallePedidoAdmin)


