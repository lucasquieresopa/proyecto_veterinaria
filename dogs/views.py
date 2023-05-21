from django.shortcuts import redirect, render

from accounts.models import CustomUser
from .forms import DogCreationForm

# Create your views here.

def dog_registration_view(request, pk):
    """definición del comportamiento de la pantalla de registro de clientes"""

    user = request.user
    if not user.is_authenticated or not user.is_veterinario:
        return redirect('home')
    
    #context = { 'usuario' : request.user}
    user_owner = CustomUser.objects.get(pk=pk)
    # context = {
    #     'user_owner': user_owner
    # }

    if request.POST:
        form = DogCreationForm(request.POST)

        if form.is_valid():
            dog = form.save(commit=False)
            dog.owner = user_owner
            #dog.owner = request.user

            dog.save()
            return redirect('home')
        
        else:
            #context['dog_registration'] = form
            context = {
                'dog_registration' : form
            }

    else:
        form = DogCreationForm()
        #context['dog_registration'] = form
        context = {
                'dog_registration' : form
            }

    return render(request, 'dog_registration.html', context)