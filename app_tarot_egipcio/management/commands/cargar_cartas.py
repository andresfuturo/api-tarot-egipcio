import json
from django.core.management.base import BaseCommand
from app_tarot_egipcio.models import CartaEgipcia

class Command(BaseCommand):
    help = "Carga cartas del Tarot Egipcio desde JSON"

    def handle(self, *args, **kwargs):
        with open('cartas_egipcias.json', encoding='utf-8') as f:
            cartas = json.load(f)
            for carta in cartas:
                CartaEgipcia.objects.update_or_create(
                    numero=carta['numero'],
                    defaults=carta
                )
        self.stdout.write(self.style.SUCCESS("Cartas cargadas correctamente."))
