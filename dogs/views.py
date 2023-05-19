from django.shortcuts import redirect, render
from accounts import forms
from accounts.models import CustomUser

from .forms import DogCreationForm, DogModificationForm
from .models import Dog

# Create your views here.

        
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

    
def dog_profile_view(request, dog_id, user_owner_id):

    if not request.user.is_authenticated:
        return redirect('login')
    
    dog = Dog.objects.get(pk=dog_id)
    user_owner = CustomUser.objects.get(pk=user_owner_id)
    print(f'dog {dog.id}, owner {user_owner.id}')
    context = {
        'dog': dog,
        'user_owner': user_owner,
    }

    return render(request, 'dog_profile.html', context)


def dog_modification_view(request, dog_id, user_owner_id):

    user = request.user
    if not user.is_authenticated or not user.is_veterinario:
        return redirect('login')
    

    dog = Dog.objects.get(id=dog_id)
    user_owner = CustomUser.objects.get(id=user_owner_id)


    if request.POST:
        #form = DogModificationForm(request.POST, user=user_owner)

        form = DogModificationForm(request.POST, instance=dog, user=user_owner)
        if form.is_valid():
            form.save()
            return redirect('dog_modification_succeed', user_owner_id=user_owner.id, dog_id=dog.id)
    else:
        form = DogModificationForm(
            initial = {
                'name': dog.name,
                'age': dog.age,
                'sex': dog.sex,
                'breed': dog.breed,
                'color': dog.color,
                'description': dog.description,
                'size': dog.size
            },
            instance=dog, 
            user=user_owner
        )
        form = DogModificationForm(instance=dog, user=user_owner)
    

    return render(request, 'dog_modification.html', {
                                                    'dog': dog, 
                                                    'form': form
                                                    }
    )


def dog_modification_done(request, dog_id, user_owner_id):
    return render(request, 'dog_modification_succeed.html', {
                                                            'dog_id': dog_id,
                                                            'user_owner_id': user_owner_id,
                                                            }
    )


