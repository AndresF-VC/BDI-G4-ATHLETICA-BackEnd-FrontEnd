"""
Este módulo define el formulario de modelo para gestionar la creación y edición
 de instancias de Athletes a través de Django Forms.
"""
from django import forms
from .models import Athletes

class AthletesForm(forms.ModelForm):
    class Meta:
        model  = Athletes
        fields = ['name','birth_date','gender','nationality','category','club']
        
"""
Proporciona campos para ingresar o actualizar la información de un atleta,
 incluyendo nombre, fecha de nacimiento, género y relaciones a otras tablas:
nacionalidad, categoría y club.
 """