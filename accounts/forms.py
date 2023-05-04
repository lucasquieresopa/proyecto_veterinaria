#extension de forms para personalizar el registro de clientes 

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.db import models
from django.contrib.auth import authenticate


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(help_text = "obligatorio")
    name = forms.CharField(label="Nombre")
    surname = forms.CharField(label="Apellido")
    telephone = forms.CharField(label="Teléfono")
    address = forms.CharField(label="Dirección")
    #falta pasar de Password -> Contraseña pero overrideando password quita algunas cosas

    class Meta(UserCreationForm):   #overridea los campos por defecto
        model = CustomUser
        fields = ('email', 'name', 'surname', 'telephone', 'address', 'password1',)


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ('mail', 'nombre', 'surname', 'tel', 'address')

class CustomUserAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')
    
    def clean(self):
        """se ejecuta antes del form para validar lo ingresado en el login"""
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Los datos ingresados son invalidos")
    