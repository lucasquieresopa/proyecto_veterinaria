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


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')  # cache the user object you pass in
        super(AdoptionPostForm, self).__init__(*args, **kwargs)


    def clean(self):
        """Comprueba que no exista otro post con los mismos datos"""

        if self.is_valid():
            # actual_form_data = self.cleaned_data    #dict
            # user_adoption_posts = self.user.adoptionpost_set    #django many to many
            name = self.cleaned_data['name']
            age = self.cleaned_data['age']
            sex = self.cleaned_data['sex']
            breed = self.cleaned_data['breed']
            color = self.cleaned_data['color']
            size = self.cleaned_data['size']
            origin = self.cleaned_data['origin']
            description = self.cleaned_data['description']

            if self.user.adoptionpost_set.filter(name=name, age=age, sex=sex, 
                                        breed=breed, color=color, size=size, 
                                        origin=origin, description=description):
                raise forms.ValidationError("Ya existe una publicación con exactamente la misma información")
            
            return self.cleaned_data
