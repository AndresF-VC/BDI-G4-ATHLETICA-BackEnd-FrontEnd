"""
This module defines the model form for managing the creation
 and editing of Athlete instances through Django Forms.

"""
from django import forms
from .models import Athletes

class AthletesForm(forms.ModelForm):
    class Meta:
        model  = Athletes
        fields = ['name','birth_date','gender','nationality','category','club']
        
"""
Provides fields to input or update an athlete’s information, 
including name, date of birth, gender, and relationships to other tables: nationality,
category, and club.

 """