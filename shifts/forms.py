from django import forms
from .models import Appointment

class MiVariableForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['description']


class EmailForm(forms.Form):
    
    message = forms.CharField(
        label="Mensaje para el cliente", 
        required=True,
        max_length=120,
        widget=forms.Textarea(attrs={'rows':3,'cols':50})
    )

    class Meta:
        fields = ('message',)