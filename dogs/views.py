from django.shortcuts import redirect, render
from .forms import DogCreationForm

# Create your views here.

def dog_registration_view(request, user_id):
    """definición del comportamiento de la pantalla de registro de clientes"""

    user = request.user
    if not user.is_authenticated or not user.is_veterinario:
        return redirect('home')

    context = {}
    if request.POST:
        form = DogCreationForm(request.POST)

        if form.is_valid():
            dog = form.save(commit=False)
            dog.owner = user_id
            dog.save()
            return redirect('home')
        
        else:
            context['dog_registration'] = form

    else:
        form = DogCreationForm()
        context['dog_registration'] = form

    return render(request, 'dog_registration.html', context)