# core/admin.py


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

# Registramos los modelos para que aparezcan en el panel de administrador de Django
admin.site.register(Athletes)
admin.site.register(Categories)
admin.site.register(Clubs)
admin.site.register(Coaches)
admin.site.register(Disciplines)
admin.site.register(Events)
admin.site.register(Nationalities)