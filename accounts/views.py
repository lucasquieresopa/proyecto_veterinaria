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
from django.contrib.auth.decorators import login_required
from pages.email_sending import send_mail_to_user
from django.db.models import Q
from django.db.models import Value
from django.db.models.functions import Concat


@login_required
def user_registration_view(request):
    """definición del comportamiento de la pantalla de registro de clientes"""
    user = request.user
    if not user.is_veterinario:
        return redirect('home')

    context = {}
    if request.POST:
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            password = get_random_string(length=6)

            user = form.save(commit=False)
            user.set_password(password)
            email = form.cleaned_data['email']
            
            send_mail_to_user("Registro exitoso en Oh My Dog!",
                              f"Usted fue registrado en la aplicación de Oh My Dog!\nSu usuario es {email} y su contraseña es {password}\nSi desea cambiar su contraseña ingrese por primera vez con la contraseña brindada, busque la opción 'Cambiar contraseña' y elija una contraseña que le agrade.\n\nSaludos,\nEquipo de Oh My Dog!",
                               "ohmydog@gmail.com",
                                [email])

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



@login_required
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

@login_required
def account_modif_done(request):
    return render(request, 'registration/account_modif_succeed.html')



# def password_reset_view(request):

#     context = {}
#     if request.POST:

#         form = CustomResetPasswordForm(request.POST)
#         if form.is_valid():
            
#             send_mail_to_user("Solicitud de cambio de contraseña para cuenta en Oh My Dog!", 
#                         f"Has solicitado cambiar la contraseña de tu cuenta \n link:",
#                         "ohmydog@gmail.com", 
#                         [form.cleaned_data['email']])

#             return redirect('password_reset_complete')
#     else:
#         form = CustomResetPasswordForm()
#     context['form'] = form
#     return render(request, 'registration/password_reset_mail_form.html', context)


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "registration/password_change_done.html"


@login_required
def list_users(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if not request.user.is_veterinario:
        return redirect('home')
    users = CustomUser.objects.filter(is_veterinario=False, is_admin=False)
    return render(request, 'list_users.html', {'users': users})



@login_required
def profile_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user_owner = CustomUser.objects.get(pk=pk)
    dogs = user_owner.dog_set.all()

    context = {
        'client': user_owner, 
        'vet': request.user, 
        'dogs_shown': dogs.filter(hidden=False)
    }
    return render(request, 'profile.html', context)

@login_required
def search_user(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if not request.user.is_veterinario:
        return redirect('home')
    if request.method == 'POST':
        buscado = request.POST['buscado']

        # users = CustomUser.objects.filter(Q(name__contains=buscado[0]) | Q(surname__contains=buscado[0]
        #                                     | Q(name__contains=buscado[1] | Q(surname__contains=buscado[1]))))
        #users = CustomUser.objects.filter(user=buscado[0])

        concatenated_names = CustomUser.objects.annotate(full_name=Concat('name', Value(' '), 'surname'))
        users = concatenated_names.filter(full_name__icontains=buscado)

        return render(request, 'search_results.html', {'buscado': buscado, 'users': users})
    else:
        return redirect(request, 'search_results.html',{})
            


