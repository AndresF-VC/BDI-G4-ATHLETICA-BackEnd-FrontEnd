"""
Este módulo define la configuración de la aplicación 'core' para Django.
Contiene la clase CoreConfig, que indica a Django el nombre de la app y el tipo
de campo de clave primaria (ID) por defecto para los modelos.
"""
from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
