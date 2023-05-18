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

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = ('nombre', 'raza', 'edad')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del perro'}),
            'raza': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Raza del perro'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad del perro'}),
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PerroForm, self).__init__(*args, **kwargs)
    
    def save(self, commit=True):
        instance = super(PerroForm, self).save(commit=False)
        instance.dueno = self.user
        if commit:
            instance.save()
        return instance
