from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.

class SignUpView(generic.CreateView):
    """SignUpView es subclase de CreateView"""

    form_class = CustomUserCreationForm   
    success_url = reverse_lazy('login')  #indica que ante un registro exitoso se redirija al template 'login'.
                                        #reverse_lazy() y no reverse() porque para las generic class-based views 
                                        # las URL no se cargan cuando se importa el archivo, entonces reverse_lazy() 
                                        # las ejecuta cuando esten disponibles
    template_name = 'registration/signup.html'