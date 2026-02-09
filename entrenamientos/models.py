from django.db import models
from django.contrib.auth.models import User

class Rutina(models.Model):

    TIPO_CHOICES = [
        ('cardio', 'Cardio'),
        ('fuerza', 'Fuerza'),
        ('hipertrofia', 'Hipertrofia'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    descripcion = models.TextField()


    imagen = models.ImageField(
        upload_to='rutinas/',
        null=True,
        blank=True
    )

    creada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre