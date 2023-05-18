from django.shortcuts import redirect, render
from .forms import DogCreationForm

# Create your views here.

def dog_registration_view(request):
    """definición del comportamiento de la pantalla de registro de clientes"""

    context = {}
    if request.POST:
        form = DogCreationForm(request.POST)

        if form.is_valid():
            
            return redirect('home')
        
        else:
            context['dog_registration'] = form

    else:
        form = DogCreationForm()
        context['dog_registration'] = form

    return render(request, 'dog_registration.html', context)