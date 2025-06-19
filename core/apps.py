"""
This module defines the configuration for the ‘core’ 
Django app. It contains the CoreConfig class, which specifies the app’s 
name and the default primary key field type (ID) for its models.

"""
from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
