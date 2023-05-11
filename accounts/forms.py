#extension de forms para personalizar el registro de clientes 

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from .models import CustomUser
from django.db import models
from django.contrib.auth import authenticate


class UserCreationForm(UserCreationForm):
    """
    overridea UserCreationForm para que las contraseñas sean opcionales.
    """

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        # If one field gets autocompleted but not the other, our 'neither
        # password or both password' validation will be triggered.
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = super(UserCreationForm, self).clean_password2()
        if bool(password1) ^ bool(password2):
            raise forms.ValidationError("Complete ambas contraseñas")
        return password2


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(help_text = "obligatorio")
    name = forms.CharField(label="Nombre", required=True)
    surname = forms.CharField(label="Apellido", required=False)
    telephone = forms.CharField(label="Teléfono", required=False)
    address = forms.CharField(label="Dirección", required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(),
                                label="Contraseña", 
                                help_text="Opcionalmente ingrese una contraseña para el cliente")
    password2 = forms.CharField(widget=forms.PasswordInput(),
                                label="Repetir contraseña", 
                                help_text="Si ingresó una contraseña, repitala")
    #falta pasar de Password -> Contraseña pero overrideando password quita algunas cosas

    class Meta(UserCreationForm):   #overridea los campos por defecto
        model = CustomUser
        fields = ('email', 'name', 'surname', 'telephone', 'address')


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ('mail', 'nombre', 'surname', 'tel', 'address')

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

    email = forms.EmailField(help_text = "obligatorio")
    name = forms.CharField(label="Nombre", required=True)
    surname = forms.CharField(label="Apellido", required=False)
    telephone = forms.CharField(label="Teléfono", required=False)
    address = forms.CharField(label="Dirección", required=False)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'surname', 'telephone', 'address')
        error_messages = {
            'email': {
                "unique": "El email ingresado ya se encuentra en uso",
            },
        }

        def clean_email(self):
            if self.is_valid():
                email = self.cleaned_data['email']
                try:
                    account = CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)  #chequea que no exista
                except CustomUser.DoesNotExist:
                    return email
                raise forms.ValidationError('Email "%s" está en uso' % email)
        
        def clean_name(self):
            if self.is_valid():
                name = self.cleaned_data['name']
                return name

        def clean_surname(self):
            if self.is_valid():
                surname = self.cleaned_data['surname']
                return surname
        
        def clean_address(self):
            if self.is_valid():
                address = self.cleaned_data['address']
                return address
        
        def clean_telephone(self):
            if self.is_valid():
                telephone = self.cleaned_data['telephone']
                return telephone

# class PasswordChangeForm(SetPasswordForm):
#     """
#     A form that lets a user change their password by entering their old
#     password.
#     """

#     error_messages = {
#         #**SetPasswordForm.error_messages,
#         "password_incorrect": "La contraseña ingresada es incorrecta",
#     }
#     old_password = forms.CharField(
#         label="Contraseña actuuuual",
#         strip=False,
#         widget=forms.PasswordInput(
#             attrs={"autocomplete": "current-password", "autofocus": True}
#         ),
#     )

#     field_order = ["old_password", "new_password1", "new_password2"]

    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages["password_incorrect"],
                code="password_incorrect",
            )
        return old_password

class PasswordResetForm(forms.ModelForm):
    email = forms.CharField(label="Email")

    class Meta:
        model = CustomUser
        fields=('email',)
        error_messages = {
            'email': {
                "unique": "El mail ingresado no se encuentra registrado",
            },
        }

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            if CustomUser.objects.filter(email=email).exists():
                return email
            else:
                raise forms.ValidationError("El mail ingresado no se encuentra registrado")