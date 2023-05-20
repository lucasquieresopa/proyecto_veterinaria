from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm, CustomUserModificationForm, CustomResetPasswordForm, CustomPasswordChangeForm
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
#from dogs.views import dog_registration_view
#from django.contrib.auth.decorators import login_required


def user_registration_view(request):
    """definición del comportamiento de la pantalla de registro de clientes"""
    user = request.user
    if not user.is_authenticated or not user.is_veterinario:
        return redirect('home')

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

            user.save()
            #dog_context['dog_registration'] 
            
            return redirect('dog_registration', pk=user.id)
     
        
        else:
            context['registration_form'] = form

    else:
        form = CustomUserCreationForm()
        context['registration_form'] = form

    context["user"] = user
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
        if form.is_valid:
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
    

    if request.POST:
        form = CustomUserModificationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account_modif_succeed')
    
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
    
    return render(request, 'registration/account_modif.html', {'account_form': form})


def account_modif_done(request):
    return render(request, 'registration/account_modif_succeed.html')



def password_reset_view(request):

    context = {}

    if request.POST:
        form = CustomResetPasswordForm(request.POST)
        if form.is_valid():
            #form.save()
            return redirect('password_reset_done')
    else:
        form = CustomResetPasswordForm()
    context['form'] = form
    return render(request, 'registration/password_reset_form.html', context)


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "registration/password_change_done.html"



def list_users(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if not request.user.is_veterinario:
        return redirect('home')
    users = CustomUser.objects.filter(is_veterinario=False, is_admin=False)
    return render(request, 'list_users.html', {'users': users})


def profile_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user_owner = CustomUser.objects.get(pk=pk)
    dogs = user_owner.dog_set.all()

    context = {
        'user': user_owner, 
        'actual_user': request.user, 
        'dogs_shown': dogs.filter(hidden=False)
    }
    return render(request, 'profile.html', context)

    
def search_user(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if not request.user.is_veterinario:
        return redirect('home')
    if request.method == 'POST':
        buscado = request.POST['buscado']
        users = CustomUser.objects.filter(name__contains=buscado)
        return render(request, 'search_results.html', {'buscado': buscado, 'users': users})
    else:
        return redirect(request, 'search_results.html',{})
            


