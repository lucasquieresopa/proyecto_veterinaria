from django import forms
from .models import Dog

class DogCreationForm(forms.ModelForm):

    name = forms.CharField(label="Nombre", required=True, help_text="*")
    age = forms.IntegerField(label="Edad (aproximada)", required=True, help_text="*")
    sex = forms.CharField(label="Sexo", required=True, help_text="*")
    breed = forms.CharField(label="Raza", required=True, help_text="*")
    color = forms.CharField(label="Color", required=False)
    size = forms.CharField(label="Tamaño", required=False)
    description = forms.CharField(label="Descripción", required=False)

    class Meta:  
        model = Dog
        fields = ('name', 'age', 'sex', 'breed', 'color', 'size', 'description')


    def __init__(self, *args, **kwargs):
      self.user = kwargs.pop('user')  # cache the user object you pass in
      super(DogCreationForm, self).__init__(*args, **kwargs)


    def clean(self):
        """se ejecuta antes del form para validar lo ingresado en el login"""
        if self.is_valid():
            name = self.cleaned_data['name']

            if self.user.dog_set.filter(name=name).exists():
                raise forms.ValidationError('El cliente ya posee un perro con ese nombre.')

        return self.cleaned_data
    
#class DogModificationForm():