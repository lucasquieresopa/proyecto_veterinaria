from django.shortcuts import redirect, render
from accounts import forms
from accounts.models import CustomUser

from .forms import DogCreationForm
from .models import Dog

# Create your views here.
def clean_name(name, user_owner):

        user_dogs = user_owner.dog_set.all()
        # try:
        #     user_dogs.filter(name=name).exists()
        # except name.DoesNotExist:
        #     return name
        # raise forms.ValidationError('El nombre "%s" ya pertenece a un perro del usuario' % name)
        if user_dogs.filter(name=name).exists():
            return name
        else:
            raise forms.ValidationError('El nombre "%s" ya pertenece a un perro del usuario' % name)

        
def dog_registration_view(request, pk):
    """definición del comportamiento de la pantalla de registro de clientes"""

    user = request.user
    if not user.is_authenticated or not user.is_veterinario:
        return redirect('home')
    
    user_owner = CustomUser.objects.get(pk=pk)


    if request.POST:
        form = DogCreationForm(request.POST, user=user_owner)

        if form.is_valid():
            #clean_name(name=request.POST['name'], user_owner=user_owner)
            # if user_owner.dog_set.filter(name=request.POST['name']).exists():
            #     raise forms.ValidationError('El cliente ya posee un perro con ese nombre.')
            

            dog = form.save(commit=False)
            dog.owner = user_owner
            dog.save()
            return redirect('home')
        
        else:
            #context['dog_registration'] = form
            context = {
                'dog_registration' : form
            }

    else:
        form = DogCreationForm(user=user_owner)
        #context['dog_registration'] = form
        context = {
                'dog_registration' : form
            }

    return render(request, 'dog_registration.html', context)

    
def dog_profile_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    dog = Dog.objects.get(pk=pk)
    context = {
        'dog': dog,
    }

    return render(request, 'dog_profile.html', context)