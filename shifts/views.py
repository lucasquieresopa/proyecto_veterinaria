from django.shortcuts import render, redirect
#from .forms import CustomUserCreationForm, CustomUserAuthenticationForm, CustomUserModificationForm, CustomResetPasswordForm, CustomPasswordChangeForm
# from django.views import generic
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.hashers import make_password
from django.contrib import messages
#from .models import CustomUser
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage
from accounts.models import CustomUser 

