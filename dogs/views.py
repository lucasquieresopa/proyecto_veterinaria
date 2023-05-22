from django.shortcuts import redirect, render
from accounts import forms
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required

from .forms import DogCreationForm, DogModificationForm, AttentionRegisterForm, VaccinationRegisterForm
from .models import Dog

from django.http import JsonResponse

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
            dog = form.save(commit=False)
            dog.owner = user_owner
            dog.save()
            return redirect('dog_registration_succeed', user_owner_id=user_owner.id)
        
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

    
def dog_registration_done(request, user_owner_id):
    return render(request, 'dog_registration_succeed.html', {
                                                            'client_id': user_owner_id,
                                                            }
    )

@login_required
def dog_profile_view(request, dog_id, user_owner_id):

    # if not request.user.is_authenticated:
    #     return redirect('login')
    
    dog = Dog.objects.get(pk=dog_id)
    user_owner = CustomUser.objects.get(pk=user_owner_id)
    context = {
        'dog': dog,
        'user_owner': user_owner,
    }

    return render(request, 'dog_profile.html', context)


@login_required
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
                'date_of_birth': dog.date_of_birth,
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

@login_required
def dog_modification_done(request, dog_id, user_owner_id):
    return render(request, 'dog_modification_succeed.html', {
                                                            'dog_id': dog_id,
                                                            'user_owner_id': user_owner_id,
                                                            }
    )

@ login_required
def hide_dog(request, dog_id):
    if request.POST.get('action') == 'post':
        #dog_id = int(request.POST.get('dog_id'))
        dog = Dog.objects.get(id=dog_id)
        print(dog.hidden)
        dog.hidden = True
        dog.save()
        print(dog.hidden)
    return JsonResponse({'hidden': True})


@ login_required
def hidden_dogs_view(request, user_id):

    user = CustomUser.objects.get(id=user_id)
    hidden_dogs = user.dog_set.filter(hidden=True)

    context = {
        'user_id': user_id,
        'hidden_dogs': hidden_dogs,
    }
    return render(request, 'hidden_dogs_list.html', context)



@login_required
def attention_registration_view(request, dog_id, client_id):
    """definición del comportamiento de la pantalla de registro de clientes"""

    actual_dog = Dog.objects.get(pk=dog_id)

    if request.POST:
        #form = AttentionRegisterForm(request.POST, dog=actual_dog)
        form = AttentionRegisterForm(request.POST)

        if form.is_valid():
            attention = form.save(commit=False)
            attention.dog = actual_dog
            attention.save()
            return redirect('dog_profile', user_owner_id=client_id, dog_id=actual_dog.id)
        
        else:
            context = {
                'attention_form' : form
            }
    else:
        #form = AttentionRegisterForm(dog=actual_dog)
        form = AttentionRegisterForm()

        context = {
                'attention_form' : form
                }
        
    return render(request, 'attention_form.html', context)


@ login_required
def attentions_list(request, dog_id, client_id):

    actual_dog = Dog.objects.get(pk=dog_id)
    attentions = actual_dog.attention_set.all()

    context = {
        'client_id': client_id,
        'dog_id': actual_dog.id,
        'attentions': attentions,
    }
    return render(request, 'attentions_list.html', context)


@login_required
def vaccination_registration_view(request, dog_id, client_id):
    """definición del comportamiento de la pantalla de registro de clientes"""

    actual_dog = Dog.objects.get(pk=dog_id)

    if request.POST:
        #form = AttentionRegisterForm(request.POST, dog=actual_dog)
        form = VaccinationRegisterForm(request.POST, dog=actual_dog)

        if form.is_valid():
            attention = form.save(commit=False)
            attention.dog = actual_dog
            attention.save()
            return redirect('dog_profile', user_owner_id=client_id, dog_id=actual_dog.id)
        
        else:
            context = {
                'vaccination_form' : form
            }
    else:
        #form = AttentionRegisterForm(dog=actual_dog)
        form = VaccinationRegisterForm(dog=actual_dog)

        context = {
                'vaccination_form' : form
                }
        
    return render(request, 'vaccination_form.html', context)


@ login_required
def vaccinations_list(request, dog_id, client_id):

    actual_dog = Dog.objects.get(pk=dog_id)
    vaccinations = actual_dog.vaccination_set.all()

    context = {
        'client_id': client_id,
        'dog_id': actual_dog.id,
        'vaccinations': vaccinations,
    }
    return render(request, 'vaccinations_list.html', context)