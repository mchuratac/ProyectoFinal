from django.urls import path
from .views import TipoIngredienteApiList

urlpatterns = [
    path('list_tipoingrediente/', TipoIngredienteApiList.as_view)
]

