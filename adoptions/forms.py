from django import forms
from .models import AdoptionPost
from dogs.models import Dog


class AdoptionPostForm(forms.ModelForm):

    name = forms.CharField(
        label="Nombre", 
        required=True, 
        help_text="*",
        max_length=30,
    )
    age = forms.CharField(
        label="Edad aproximada", 
        required=True, 
        help_text="*",
        max_length=30,
    )
    sex = forms.CharField(
        label="Sexo", 
        required=True, 
        help_text="*",
        widget=forms.Select(choices=Dog.Sex.choices),
    )
    breed = forms.CharField(
        label="Raza", 
        required=True, 
        help_text="*",
        widget=forms.Select(choices=Dog.Breed.choices),
    )
    color = forms.CharField(
        label="Color", 
        required=True,
        help_text="*",
        widget=forms.Select(choices=Dog.Color.choices),
    )
    size = forms.CharField(
        label="Tamaño", 
        required=True,
        help_text="*",
        widget=forms.Select(choices=Dog.Size.choices),
    )
    origin = forms.CharField(
        label="Lugar de procedencia", 
        required=True,
        help_text="*",
        widget=forms.Select(choices=AdoptionPost.Origin.choices),
    )
    description = forms.CharField(
        label="Descripción", 
        required=False,
        max_length=120,
    )

    class Meta:  
        model = AdoptionPost
        fields = ('name', 'age', 'sex', 'breed', 'color', 'size', 'origin', 'description')


    # def __init__(self, *args, **kwargs):
    #     self.post = kwargs.pop('post')  # cache the user object you pass in
    #     super(AdoptionPostForm, self).__init__(*args, **kwargs)


    # def clean(self):
    #     if self.is_valid():
    #         name = self.cleaned_data['name']

    #         if self.user.dog_set.filter(name=name).exists():
    #             raise forms.ValidationError('El cliente ya posee un perro con ese nombre.')

    #     return self.cleaned_data