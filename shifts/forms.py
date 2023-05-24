from django import forms
from .models import Appointment

class MiVariableForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['description']
