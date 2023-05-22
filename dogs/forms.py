from django import forms
from .models import Dog, Attention, Vaccination

class DogCreationForm(forms.ModelForm):

    name = forms.CharField(
        label="Nombre", 
        required=True, 
        help_text="*"
    )
    date_of_birth = forms.DateField(
        label="Fecha de nacimiento",
        required=True,
        help_text="*",
        widget=forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})
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
        required=False
    )

    class Meta:  
        model = Dog
        fields = ('name', 'date_of_birth', 'sex', 'breed', 'color', 'size', 'description')
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')  # cache the user object you pass in
        super(DogCreationForm, self).__init__(*args, **kwargs)


    def clean(self):
        if self.is_valid():
            name = self.cleaned_data['name']

            if self.user.dog_set.filter(name=name).exists():
                raise forms.ValidationError('El cliente ya posee un perro con ese nombre.')

        return self.cleaned_data
    

class DogModificationForm(forms.ModelForm):

    name = forms.CharField(
        label="Nombre", 
        required=True, 
        help_text="*"
    )
    date_of_birth = forms.DateField(
        label="Fecha de nacimiento",
        required=True,
        help_text="*",
        widget=forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})
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
        required=False,
        widget=forms.Select(choices=Dog.Color.choices),
    )
    size = forms.CharField(
        label="Tamaño", 
        required=False,
        widget=forms.Select(choices=Dog.Size.choices),
    )
    description = forms.CharField(
        label="Descripción", 
        required=False
    )

    class Meta:  
        model = Dog
        fields = ('name', 'date_of_birth', 'sex', 'breed', 'color', 'size', 'description')
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')  # cache the user object you pass in
        super(DogModificationForm, self).__init__(*args, **kwargs)


    def clean_name(self):
 
        name = self.cleaned_data['name']
    
        try:
            idk = self.user.dog_set.exclude(pk=self.instance.pk).get(name=name)  #chequea que no exista
        except Dog.DoesNotExist:
            return name
        raise forms.ValidationError('El nombre "%s" está en uso' % name)
    
        
        
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        return date_of_birth

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
    

class AttentionRegisterForm(forms.ModelForm):

    type = forms.CharField(
        label="Tipo de atención", 
        required=True, 
        help_text="*",
        widget=forms.Select(choices=Attention.Type.choices)
    )
    description = forms.CharField(
        label="Descripción", 
        required=False, 
    )

    class Meta:  
        model = Attention
        fields = ('type', 'description')


class VaccinationRegisterForm(forms.ModelForm):

    type = forms.CharField(
        label="Tipo de vacuna", 
        required=True, 
        help_text="*",
        widget=forms.Select(choices=Vaccination.Type.choices)
    )
    brand = forms.CharField(
        label="Marca", 
        required=True, 
        help_text="*",
    )
    lot = forms.CharField(
        label="Lote", 
        required=True, 
        help_text="*",
    )
    dosis_number = forms.IntegerField(
        min_value=1,
        required=True, 
        help_text="*",

    )
    total_dosis = forms.IntegerField(
        min_value=1,
        required=True, 
        help_text="*",
    )
    date_of_application = forms.DateField(
        required=True, 
        help_text="*",
        widget=forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})
    )

    class Meta:  
        model = Vaccination
        fields = ('type', 'brand', 'lot', 'dosis_number', 'total_dosis', 'date_of_application')