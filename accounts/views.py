from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm
# from django.urls import reverse_lazy
# from django.views import generic
from django.contrib.auth import login, authenticate, logout


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
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
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