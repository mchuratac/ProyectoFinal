from django.shortcuts import render
from rest_framework import generics
from .serializers import TipoIngredienteSerializer
from .models import TipoIngrediente

# Create your views here.

class TipoIngredienteApiList(generics.ListAPIView):
    queryset = TipoIngrediente.objects.all()
    serializer_class = TipoIngredienteSerializer
