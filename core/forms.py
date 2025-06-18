from django import forms
from .models import Athletes

class AthletesForm(forms.ModelForm):
    class Meta:
        model  = Athletes
        fields = ['name','birth_date','gender','nationality','category','club']
