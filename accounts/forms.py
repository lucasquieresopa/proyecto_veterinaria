#extension de forms para personalizar el registro de clientes 

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):   #overridea los campos por defecto
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('name',)
        #fields = UserCreationForm.Meta.fields + ('name', 'surname', 'tel', 'address')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields