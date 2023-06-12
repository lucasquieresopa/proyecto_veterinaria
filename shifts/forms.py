from datetime import date
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


class ReprogramEmailForm(forms.Form):

    
    date_of_shift = forms.DateField(
        label="Fecha de turno reprogramado",
        required=True, 
        help_text="*",
        widget=forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
    )
    hour = forms.CharField(
        label="Horario", 
        required=True, 
        help_text="*",
        widget=forms.Select(choices=Appointment.Hour.choices),
    )

    message = forms.CharField(
        label="Mensaje para el cliente", 
        required=True,
        max_length=120,
        widget=forms.Textarea(attrs={'rows':3,'cols':50})
    )

    class Meta:
        fields = ('date_of_shift', 'hour', 'message',)

    
    def clean_date_of_shift(self):
        if self.is_valid():
            shift_date = self.cleaned_data['date_of_shift']
 
            if shift_date <= date.today():
                raise forms.ValidationError('Debe elegir una fecha posterior a la fecha de hoy')
            else:
                return self.cleaned_data['date_of_shift']
            