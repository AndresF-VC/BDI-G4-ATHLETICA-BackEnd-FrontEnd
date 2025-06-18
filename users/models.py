# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Heredamos: username, password, email, first_name, last_name, etc.
    
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('coach', 'Entrenador'),
        ('athlete', 'Atleta'),
        ('guest', 'Invitado'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='guest')
    
    # Las relaciones con Athlete y Coach que tenías en tu SQL original.
    # Ahora que los modelos existen, podemos definirlas.
    # related_name es útil para las consultas inversas.
    athlete = models.ForeignKey('core.Athletes', on_delete=models.SET_NULL, null=True, blank=True, related_name='user_profile')
    coach = models.ForeignKey('core.Coaches', on_delete=models.SET_NULL, null=True, blank=True, related_name='user_profile')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'olympus"."users'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'