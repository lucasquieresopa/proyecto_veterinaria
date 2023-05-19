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
        if self.is_valid():
            name = self.cleaned_data['name']

            if self.user.dog_set.filter(name=name).exists():
                raise forms.ValidationError('El cliente ya posee un perro con ese nombre.')

        return self.cleaned_data
    
class DogModificationForm(forms.ModelForm):

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
        super(DogModificationForm, self).__init__(*args, **kwargs)


    def clean_name(self):
 
        if self.is_valid():
            name = self.cleaned_data['name']
    
            try:
                idk = self.user.dog_set.exclude(pk=self.instance.pk).get(name=name)  #chequea que no exista
            except Dog.DoesNotExist:
                return name
            raise forms.ValidationError('El nombre "%s" está en uso' % name)
    
        
        
    def clean_age(self):
        if self.is_valid():
            age = self.cleaned_data['age']
            return age

    def clean_sex(self):
        if self.is_valid():
            sex = self.cleaned_data['sex']
            return sex
        
    def clean_breed(self):
        if self.is_valid():
            breed = self.cleaned_data['breed']
            return breed
        
    def clean_color(self):
        if self.is_valid():
            color = self.cleaned_data['color']
            return color
        
    def clean_size(self):
        if self.is_valid():
            size = self.cleaned_data['size']
            return size
        
    def clean_description(self):
        if self.is_valid():
            description = self.cleaned_data['description']
            return description