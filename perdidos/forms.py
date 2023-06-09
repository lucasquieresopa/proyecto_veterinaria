from django import forms 
from .models import LostPost
from dogs.models import Dog


class LostPostForm (forms.ModelForm):
    name = forms.CharField(
        label="Nombre", 
        required=True, 
        help_text="*",
        max_length=30,
    )
    age = forms.CharField(
        label="Edad", 
        required=True, 
        help_text="*",
        widget=forms.Select(choices=LostPost.Age.choices),
    )
    zone = forms.CharField(
        label="Zona",
        required=True,
        help_text="*",
        max_length=45,
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
    
    description = forms.CharField(
        label="Descripción", 
        required=False,
        max_length=120,
    )



    class Meta: 
        model = LostPost
        fields = ('name', 'age', 'zone', 'sex', 'breed', 'color', 'size','description') 
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')  # cache the user object you pass in
        super(LostPostForm, self).__init__(*args, **kwargs)

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
            zone = self.cleaned_data['zone']
            description = self.cleaned_data['description']

            if self.user.lostpost_set.filter(name=name, age=age, sex=sex, 
                                        breed=breed, color=color, size=size, 
                                        zone=zone, description=description):
                raise forms.ValidationError("Ya existe una publicación con exactamente la misma información para este cliente")
            
            return self.cleaned_data

class LostPostModificationForm(forms.ModelForm):

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
    zone = forms.CharField(
        label="Zona",
        required=True,
        help_text="*",
        max_length=45,
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
    
    description = forms.CharField(
        label="Descripción", 
        required=False,
        max_length=120,
    )

    class Meta:  
        model = LostPost
        fields = ('name', 'age', 'sex', 'zone','breed', 'color', 'size', 'description')


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')  # cache the user object you pass in
        super(LostPostModificationForm, self).__init__(*args, **kwargs)


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
            zone = self.cleaned_data['zone']
            description = self.cleaned_data['description']

            if self.user.lostpost_set.filter(name=name, age=age, sex=sex, 
                                        breed=breed, color=color, size=size, 
                                        zone=zone, description=description):
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

class ConfirmLostForm(forms.Form):

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
                ¿Por qué para usted es su perro?, \n
                ¿Cuándo fue que se le perdio?, \n 
                
                """,
        widget=forms.Textarea(attrs={'rows':3,'cols':50})
    )

    class Meta:  
        fields = ('email', 'telephone', 'description')