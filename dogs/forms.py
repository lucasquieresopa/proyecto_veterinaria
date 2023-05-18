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
    