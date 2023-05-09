from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm, CustomUserModificationForm
# from django.views import generic
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.hashers import make_password


# # Create your views here.

# class SignUpView(generic.CreateView):
#     """SignUpView es subclase de CreateView"""

#     form_class = CustomUserCreationForm   
#     success_url = reverse_lazy('login')  #indica que ante un registro exitoso se redirija al template 'login'.
#                                         #reverse_lazy() y no reverse() porque para las generic class-based views 
#                                         # las URL no se cargan cuando se importa el archivo, entonces reverse_lazy() 
#                                         # las ejecuta cuando esten disponibles
#     template_name = 'registration/signup.html'

def user_registration_view(request):
    """definición del comportamiento de la pantalla de registro de clientes"""

    context = {}
    if request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            #raw_password = form.cleaned_data.get('password1')
            #account = authenticate(email=email, password=raw_password)
            #login(request, account)
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

# class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
#     template_name = 'users/password_reset.html'
#     email_template_name = 'users/password_reset_email.html'
#     subject_template_name = 'users/password_reset_subject'
#     success_message = "We've emailed you instructions for setting your password, " \
#                       "if an account exists with the email you entered. You should receive them shortly." \
#                       " If you don't receive an email, " \
#                       "please make sure you've entered the address you registered with, and check your spam folder."
#     success_url = reverse_lazy('users-home')