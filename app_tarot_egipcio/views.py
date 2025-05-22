from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.utils import timezone
from random import choice
from .models import CartaEgipcia
from .serializers import CartaEgipciaSerializer

class CartaEgipciaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CartaEgipcia.objects.all()
    serializer_class = CartaEgipciaSerializer

    @action(detail=False, methods=['get'])
    def random(self, request):
        """Devuelve una carta egipcia aleatoria"""
        cartas = list(CartaEgipcia.objects.all())
        if not cartas:
            return Response({"error": "No hay cartas disponibles"}, status=status.HTTP_404_NOT_FOUND)
        
        carta_aleatoria = choice(cartas)
        serializer = self.get_serializer(carta_aleatoria)
        return Response(serializer.data)
