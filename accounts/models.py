import datetime
from typing import Optional
import warnings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin 
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """instanciacion de CustomUser"""
        if not email:
            raise ValueError("El usuario debe tener un mail")
        if not name:
            raise ValueError("El usuario debe tener un nombre")

        user = self.model(
            email=self.normalize_email(email),   #convierte los char de email a lowercase
            name=name,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(
            email=self.normalize_email(email),   #convierte los char de email a lowercase
            password=password,
            name=name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="email", 
        unique=True,
        max_length=40,
        error_messages={"unique":'El mail ya se encuentra registrado. Por favor ingrese otro.'}
    )
    name = models.CharField(
        max_length=30
    ) 
    surname = models.CharField(
        max_length=30, 
        blank=True, 
        null=True
    )
    address = models.CharField(
        max_length=30, 
        blank=True, 
        null=True
    )
    telephone = models.SlugField(
        max_length=15, 
        blank=True, 
        null=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_admin = models.BooleanField(
        default=False,
    )
    last_login = models.DateTimeField(
        verbose_name="last login", 
        default=datetime.datetime.now,
    )
    is_veterinario = models.BooleanField(
        default=False,
    )
    

    USERNAME_FIELD = "email"    #variable por la cual se ingresa, dice username pero seria como 'campo que representa el inicio de sesion'
    REQUIRED_FIELDS = ['name',]    #no permite registros si no tiene estos campos completos

    objects = CustomUserManager()

    def __str__(self):
        """cuando se imprima un objeto CustomUser se imprimira su nombre + apellido"""
        return self.name + ' ' + str(self.surname or '')

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
    