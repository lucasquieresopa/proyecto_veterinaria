from django import forms
from .models import Dog

class DogCreationForm(forms.ModelForm):

    name = forms.CharField(label="Nombre", required=True)
    age = forms.IntegerField(label="Edad (aproximada)", required=True)
    sex = forms.CharField(label="Sexo", required=True)
    breed = forms.CharField(label="Raza", required=True)

    class Meta:  
        model = Dog
        fields = ('name', 'age', 'sex', 'breed')