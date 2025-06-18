# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Añadimos nuestros campos personalizados ('role', 'athlete', 'coach')
    # a la vista de edición del usuario en el panel de admin.
    fieldsets = UserAdmin.fieldsets + (
        ('Campos Personalizados', {'fields': ('role', 'athlete', 'coach')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Personalizados', {'fields': ('role', 'athlete', 'coach')}),
    )
    # Añadimos 'role' a las columnas que se muestran en la lista de usuarios.
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_staff']

# Registramos nuestro CustomUser con su configuración de admin personalizada.
admin.site.register(CustomUser, CustomUserAdmin)