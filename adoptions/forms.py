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



class AdoptionPostModificationForm(forms.ModelForm):

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
        super(AdoptionPostModificationForm, self).__init__(*args, **kwargs)


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
        
    def clean_sex(self):
        sex = self.cleaned_data['sex']
        return sex
        
    def clean_breed(self):
        breed = self.cleaned_data['breed']
        return breed
        
    def clean_color(self):
        color = self.cleaned_data['color']
        return color
        
    def clean_size(self):
        size = self.cleaned_data['size']
        return size
        
    def clean_description(self):
        description = self.cleaned_data['description']
        return description



class ConfirmAdoptionForm(forms.Form):

    email = forms.EmailField(
        max_length=40,
    )
    telephone = forms.CharField(
        label="Teléfono", 
        required=True,
        max_length=15,
    )
    description = forms.CharField(
        label="Mensaje", 
        required=True,
        max_length=120,
        help_text="""\n
                Brinde una pequeña descripción de su situación. Algunos disparadores:\n
                ¿Por qué este perro es correcto para usted?, \n
                ¿Cuántos perros tiene actualmente?, \n 
                ¿Tiene patio?
                """,
        widget=forms.Textarea(attrs={'rows':3,'cols':50})
    )

    class Meta:  
        fields = ('email', 'telephone', 'description')