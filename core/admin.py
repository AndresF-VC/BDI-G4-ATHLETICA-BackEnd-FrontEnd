
"""
In this module, the sports-domain models are registered so they’re enabled in Django’s admin site.
This makes it possible to manage the main tables (Athletes, Categories, Clubs, Coaches, Disciplines, 
Events, Nationalities) via the admin interface: creating, editing, listing, and deleting.

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
# Registering models in the Django admin panel
# Each call to admin.site.register enables management of the corresponding table
# without the need to create custom views or forms.
admin.site.register(Athletes)    
admin.site.register(Categories) 
admin.site.register(Clubs)      
admin.site.register(Coaches)     
admin.site.register(Disciplines) 
admin.site.register(Events)      
admin.site.register(Nationalities) 
