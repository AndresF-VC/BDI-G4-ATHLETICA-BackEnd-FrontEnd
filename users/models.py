"""
Este módulo define el modelo CustomUser, extendiendo el usuario predeterminado de Django
(AbstractUser) para incluir un campo de rol (admin, coach, athlete, guest) y establecer relaciones opcionales
con los modelos de Athletes y Coaches, permitiendo asociar cada usuario con su perfil deportivo correspondiente.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('coach', 'Entrenador'),
        ('athlete', 'Atleta'),
        ('guest', 'Invitado'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='guest')
    
    athlete = models.ForeignKey('core.Athletes', on_delete=models.SET_NULL, null=True, blank=True, related_name='user_profile')
    coach = models.ForeignKey('core.Coaches', on_delete=models.SET_NULL, null=True, blank=True, related_name='user_profile')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'olympus"."users'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'