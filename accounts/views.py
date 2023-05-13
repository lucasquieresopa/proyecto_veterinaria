from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm, CustomUserModificationForm, ResetPasswordForm, CustomPasswordChangeForm
# from django.views import generic
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import CustomUser
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage



# # Create your views here.


def user_registration_view(request):
    """definición del comportamiento de la pantalla de registro de clientes"""

    context = {}
    if request.POST:
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            password = get_random_string(length=6)
            user = form.save(commit=False)
            user.set_password(password)
            email = form.cleaned_data['email']
            mail = EmailMessage(
                                "Registro exitoso", 
                                "La contraseña para {} es {}".format(email, password), 
                                "ohmydog@@gmail.com",
                                ["e12436402b811a@inbox.mailtrap.io"]
            )
            mail.send()
            form.save()
            
            
            return redirect('login')
        
        else:
            context['registration_form'] = form

    else:
        form = CustomUserCreationForm()
        context['registration_form'] = form

    return render(request, 'registration/client_registration.html', context)





def logout_view(request):
    """definicion del logout, mas intuitiva que hacerlo con constantes como hace la guia"""
    logout(request)
    return redirect('login')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')
    
    if request.POST:
        form = CustomUserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')
    
    else:
        form = CustomUserAuthenticationForm()
    
    context['login_form'] = form
    return render(request, 'registration/login.html', context)


def account_modif_view(request):

    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {}

    if request.POST:
        form = CustomUserModificationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    
    else:
        form = CustomUserModificationForm(
            initial = {
                "email": request.user.email,
                "name": request.user.name,
                "surname": request.user.surname,
                "telephone": request.user.telephone,
                "address": request.user.address
            }
        )
    
    context['account_form'] = form
    return render(request, 'registration/account_modif.html', context)


def password_reset_view(request):

    context = {}

    if request.POST:
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            #form.save()
            return redirect('password_reset_done')
    else:
        form = ResetPasswordForm()
    context['form'] = form
    return render(request, 'registration/password_reset_form.html', context)

#INTERNAL_RESET_SESSION_TOKEN = "_password_reset_token"

# class CustomChangePasswordView(PasswordChangeView):
#     form_class = CustomPasswordChangeForm
#     success_url = reverse_lazy('password_change_done')


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "registration/password_change_done.html"




# def password_change(request):
#     #user is authenticated?
#     user = request.user
#     if request.method == 'POST':
#         form = SetPasswordForm(user, request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Tu contraseña fue cambiada")
#             return redirect('login')
#         else:
#             for error in list(form.errors.values()):
#                 messages.error(request, error)

#     form = SetPasswordForm(user)
#     return render(request, 'password_reset_confirm.html', {'form': form})



# class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
#     template_name = 'users/password_reset.html'
#     email_template_name = 'users/password_reset_email.html'
#     subject_template_name = 'users/password_reset_subject'
#     success_message = "We've emailed you instructions for setting your password, " \
#                       "if an account exists with the email you entered. You should receive them shortly." \
#                       " If you don't receive an email, " \
#                       "please make sure you've entered the address you registered with, and check your spam folder."
#     success_url = reverse_lazy('users-home')

