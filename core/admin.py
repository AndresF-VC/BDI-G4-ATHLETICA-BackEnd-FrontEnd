
"""
En este módulo se registran los modelos del dominio deportivo para habilitarlos
en el sitio de administración de Django. Esto permite gestionar las tablas principales
(Athletes, Categories, Clubs, Coaches, Disciplines, Events, Nationalities) desde la
interfaz de administración: creación, edición, listado y eliminación.
"""
from django.contrib import admin
from .models import (
    Athletes,
    Categories,
    Clubs,
    Coaches,
    Disciplines,
    Events,
    Nationalities,
)
# Registro de modelos en el panel de administración de Django
# Cada llamada a admin.site.register permite gestionar la tabla correspondiente
# sin necesidad de crear vistas o formularios personalizados.
admin.site.register(Athletes)    
admin.site.register(Categories) 
admin.site.register(Clubs)      
admin.site.register(Coaches)     
admin.site.register(Disciplines) 
admin.site.register(Events)      
admin.site.register(Nationalities) 
