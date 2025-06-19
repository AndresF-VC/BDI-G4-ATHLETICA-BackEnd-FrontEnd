"""
This module configures the API routes for the Core application:

* Registers the `athletes` endpoint for CRUD operations on athletes.
* Adds read-only endpoints to retrieve lists of nationalities, categories, and clubs.

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