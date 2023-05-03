from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.

class SignupView(generic.CreateView):
    """SignedView es subclase de CreateView"""

    form_class = UserCreationForm   
    success_url = reverse_lazy('home')  #indica que ante un registro exitoso se redirija al template 'home.
                                        #reverse_lazy() y no reverse() porque para las generic class-based views 
                                        # las URL no se cargan cuando se importa el archivo, entonces reverse_lazy() 
                                        # las ejecuta cuando esten disponibles
    template_name = 'registration/signup.html'