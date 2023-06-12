from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList 
from .models import LostPost
from dogs.models import Dog
from django.template.defaultfilters import linebreaksbr


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
    zone = forms.CharField(
        label="Zona donde se perdió", 
        required=True,
        help_text="*",
    )
    image = forms.ImageField(
        label="Foto del perro:",
        required=True,
        help_text="*",
    )

    
    class Meta: 
        model = LostPost
        fields = ('name', 'age', 'zone', 'sex', 'breed', 'color', 'size', 'image') 

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
            zone = self.cleaned_data['zone']
            breed = self.cleaned_data['breed']
            color = self.cleaned_data['color']
            size = self.cleaned_data['size']

            if LostPost.objects.filter(name__iexact=name, age=age, sex=sex, zone=zone,
                                        breed=breed, color=color, size=size
                                        ):
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
        
    def clean_zone(self):
        zone = self.cleaned_data['zone']
        return zone


    
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
        widget=forms.Select(choices=LostPost.Age.choices),
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

    zone = forms.CharField(
        label="Zona donde se perdió", 
        required=True,
        help_text="*",
    )
    image = forms.ImageField(
        label="Foto del perro:",
        required=True,
        help_text="*",
    )
    

    class Meta:  
        model = LostPost
        fields = ('name', 'age', 'sex', 'breed', 'color', 'size', 'zone', 'image')


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

<<<<<<< HEAD
            if self.user.lostpost_set.exclude(id=self.instance.id).filter(name=name, age=age, sex=sex, 
=======
            if LostPost.objects.filter(name__iexact=name, age=age, sex=sex, 
>>>>>>> 5362802aefb1504a8d5b019931192a7b461afebc
                                        breed=breed, color=color, size=size, 
                                        zone=zone).exclude(id=self.instance.id):
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
        
    def clean_zone(self):
        description = self.cleaned_data['zone']
        return description
    
class ConfirmFoundForm(forms.Form):

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
        help_text=linebreaksbr('\nBrinde una pequeña descripción de su situación. Algunos disparadores:\n¿Dónde encontró al perro?, \nAlguna caractrerística particular del perro, \n Alguna actitud particular'),
        widget=forms.Textarea(attrs={'rows':3,'cols':50})
    )

    class Meta:  
        fields = ('email', 'telephone', 'description',)