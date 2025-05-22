from rest_framework import serializers
from .models import CartaEgipcia

class CartaEgipciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartaEgipcia
        fields = '__all__'
