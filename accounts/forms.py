#extension de forms para personalizar el registro de clientes 

#from django import forms
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from .models import CustomUser
#from django.db import models


# class CustomUserCreationForm(UserCreationForm):
#     email = models.EmailField(help_text = "obligatorio")

#     class Meta(UserCreationForm):   #overridea los campos por defecto
#         model = CustomUser
#         fields = ('Mail', 'Nombre', 'Apellido', 'Telefono', 'Direccion')


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ('mail', 'nombre', 'surname', 'tel', 'address')