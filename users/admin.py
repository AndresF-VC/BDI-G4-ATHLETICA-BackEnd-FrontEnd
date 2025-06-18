"""
Configura la administración de Django para el modelo CustomUser,
extendiendo la interfaz por defecto (UserAdmin) para:
- Incluir los campos personalizados 'role', 'athlete' y 'coach' en los formularios de creación y edición.
- Mostrar el campo 'role' junto con la información básica en la lista de usuarios.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Campos Personalizados', {'fields': ('role', 'athlete', 'coach')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Personalizados', {'fields': ('role', 'athlete', 'coach')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)