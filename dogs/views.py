from django.shortcuts import redirect, render
from .forms import DogCreationForm

# Create your views here.

def dog_registration_view(request):
    """definición del comportamiento de la pantalla de registro de clientes"""

    user = request.user
    if not user.is_authenticated or not user.is_veterinario:
        return redirect('home')

    context = {}
    if request.POST:
        form = DogCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        
        else:
            context['dog_registration'] = form

    else:
        form = DogCreationForm()
        context['dog_registration'] = form

    return render(request, 'dog_registration.html', context)