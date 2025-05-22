from django.db import models

class CartaEgipcia(models.Model):
    numero = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    significado = models.TextField()
    elemento = models.CharField(max_length=50)
    planeta = models.CharField(max_length=50)
    palabra_clave = models.CharField(max_length=50)
    mensaje = models.TextField()

    def __str__(self):
        return f"{self.numero} - {self.nombre}"
