from django.contrib import admin
from .models import CartaEgipcia

@admin.register(CartaEgipcia)
class CartaEgipciaAdmin(admin.ModelAdmin):
    list_display = (
        'numero',
        'nombre',
        'significado',
        'elemento',
        'planeta',
        'palabra_clave',
        'mensaje'
    )
