
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Rol,Ingrediente, TipoIngrediente, EstadoPedido, Pedido, DetallePedido

# Register your models here.
#class TipoIngredienteAdmin(admin.ModelAdmin):
#    list_display=['id','tipo', 'ingrediente']

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Ingrediente)
admin.site.register(TipoIngrediente)
admin.site.register(EstadoPedido)
admin.site.register(Pedido)
admin.site.register(DetallePedido)


