#extension de forms para personalizar el registro de clientes 

import gettext
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from .models import CustomUser
from django.db import models
from django.contrib.auth import authenticate, password_validation
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError



class CustomUserCreationForm(forms.ModelForm):

    email = forms.EmailField(
        help_text = "*",
        max_length=40,
    )
    name = forms.CharField(
        label="Nombre", 
        required=True, 
        help_text = "*",
        max_length=30,
    )
    surname = forms.CharField(
        label="Apellido", 
        required=True, 
        help_text = "*",
        max_length=30,
    )
    telephone = forms.CharField(
        label="Teléfono", 
        required=False,
        max_length=15,
    )
    address = forms.CharField(
        label="Dirección", 
        required=False,
        max_length=30,
    )


    class Meta:   #overridea los campos por defecto
        model = CustomUser
        fields = ('email', 'name', 'surname', 'telephone', 'address')


class CustomUserAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Contraseña', 
                               widget=forms.PasswordInput)

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



class CustomUserModificationForm(forms.ModelForm):

    email = forms.EmailField(
        help_text = "*",
        max_length=40,
    )
    name = forms.CharField(
        label="Nombre", 
        required=True, 
        help_text = "*",
        max_length=30,
    )
    surname = forms.CharField(
        label="Apellido", 
        required=True, 
        help_text = "*",
        max_length=30,
    )
    telephone = forms.CharField(
        label="Teléfono", 
        required=False,
        max_length=12,
    )
    address = forms.CharField(
        label="Dirección", 
        required=False,
        max_length=30,
    )
    
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'surname', 'telephone', 'address')
        error_messages = {
            'email': {
                "unique": "El email ingresado ya se encuentra en uso",
            },
        }

    
    def clean_email(self):
 
        email = self.cleaned_data['email']
        try:
            account = CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)  #chequea que no exista
        except CustomUser.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" está en uso' % email)
        
    def clean_name(self):
        name = self.cleaned_data['name']
        return name

    def clean_surname(self):
        surname = self.cleaned_data['surname']
        return surname

    def clean_address(self):
        address = self.cleaned_data['address']
        return address
        
    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        return telephone            


class CustomPasswordSetForm(SetPasswordForm):
    new_password = forms.CharField(label="Nueva contraseña",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'type': 'password'
                                }))
    new_password2 = forms.CharField(label="Repetir contraseña",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'type': 'password'
                                }))
    
    class Meta:
        models = CustomUser
        fields = ['new_password1', 'new_password2']


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Contraseña actual",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'type': 'password'
                                }))
    
    

class CustomResetPasswordForm(forms.Form):

    email = forms.CharField(
        label="Email", 
        required=True,
    )

    class Meta:
        fields=('email',)

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            if CustomUser.objects.filter(email=email).exists():
                return email
            else:
                raise forms.ValidationError("El mail ingresado no se encuentra registrado")
            