from django.shortcuts import render, redirect
from accounts.models import CustomUser

from perdidos.models import LostPost
from .forms import LostPostForm, LostPostModificationForm, ConfirmFoundForm
from django.contrib.auth.decorators import login_required
from pages.email_sending import send_mail_to_user
from .models import Dog

from .filtros import OrderFilter

# Create your views here.
@login_required
def dog_question_view(request, user_id):
    user_owner = CustomUser.objects.get(pk=user_id)
    dogs = user_owner.dog_set.all()

    context = { 
        'dogs':dogs.filter(hidden=False),
        'user': request.user,
        }

    return render(request, 'dog_question.html', context)


@login_required
def lost_post_form_view(request):
    user = request.user
    
    if request.POST:
        form = LostPostForm(request.POST, request.FILES, user=user)

        if form.is_valid():
            lost_post = form.save(commit=False)
            lost_post.author = user
            lost_post.save()
            return redirect('lost_post_form_succeed')  
        else:
            context = {
                'lost_post_form' : form
            }
    else:
        form = LostPostForm(user=user)
        context = {
                'lost_post_form' : form
                }
        
    return render(request, 'lost_post_form.html', context)

@login_required
def lost_post_form_preload_view(request, dog_id):
    user = request.user
    dog = Dog.objects.get(pk=dog_id)
    
    if request.POST:
        form = LostPostForm(request.POST, request.FILES, user=user)

        if form.is_valid():
            lost_post = form.save(commit=False)
            lost_post.author = user
            lost_post.save()
            return redirect('lost_post_form_succeed')   
        else:
            form = LostPostForm(user=user,
                initial={
                'name': dog.name,
                'breed': dog.breed,
                'sex': dog.sex,
                'color': dog.color,
                'size': dog.size
        })
            context = {
                'lost_post_form' : form
            }    
    else:
        form = LostPostForm(user=user,
            initial={
            'name': dog.name,
            'breed': dog.breed,
            'sex': dog.sex,
            'color': dog.color,
            'size': dog.size
        })

    context = {
        'lost_post_form': form
    }
        
    return render(request, 'lost_post_form_preload.html', context)


@login_required
def lost_post_form_succeed(request):
    return render(request, 'lost_post_form_succeed.html')


def lost_posts_list(request):
    """activa el template que muestra las publicaciones de perdidos excluyendo las del usuario"""
    lost_posts = LostPost.objects.all().order_by('-publication_date', 'was_found')


    post_filter = OrderFilter(request.GET, queryset=lost_posts)
    lost_posts = post_filter.qs

    context = {
        'posts': lost_posts,
        'actual_user_id': request.user.id,
        'filter': post_filter,
    }

    return render(request, 'lost_post_list.html', context)


@login_required
def client_lost_posts_list(request):

    client = CustomUser.objects.get(pk=request.user.id)
    client_lost_posts = client.lostpost_set.all().order_by('-publication_date', 'was_found')

    post_filter = OrderFilter(request.GET, queryset=client_lost_posts)
    client_lost_posts = post_filter.qs

    context = {
        'posts': client_lost_posts,
        'filter': post_filter,
    }

    return render(request, 'client_lost_post_list.html', context)


@login_required
def lost_post_modification(request, post_id):

    post = LostPost.objects.get(id=post_id)

    if request.POST:
        form = LostPostModificationForm(request.POST, request.FILES, instance=post, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('lost_post_modification_succeed')
    else:
        form = LostPostModificationForm(
            initial = {
                'name': post.name,
                'age': post.age,
                'sex': post.sex,
                'breed': post.breed,
                'color': post.color,
                'size': post.size,
                'zone':post.zone,
                
            },
            user=request.user,
            instance=post
        )
        form = LostPostModificationForm(instance=post, user=request.user)
    
    context = {
        'lost_post_modification_form': form,
    }

    return render(request, 'lost_post_modification_form.html', context)


@login_required
def lost_post_modification_succeed(request):
    return render(request, 'lost_post_modification_succeed.html')



def delete_lost_post(request, post_id):
    """borrado de post en la pestaña de posts propios"""
    post = LostPost.objects.get(pk=post_id)
    post.delete()
    return redirect('client_lost_posts')


def delete_lost_post_from_general(request, post_id):
    """borrado de post en la pestaña con todas las publicaciones"""
    post = LostPost.objects.get(pk=post_id)
    post.delete()
    return redirect('lost_posts')


def mark_as_found(request, post_id):
    post = LostPost.objects.get(pk=post_id)
    post.was_found = True
    post.save()
    return redirect('client_lost_posts')


def mark_as_found_from_general(request, post_id):
    post = LostPost.objects.get(pk=post_id)
    post.was_found = True
    post.save()
    return redirect('lost_posts')



def confirm_found(request, post_id):
    post = LostPost.objects.get(pk=post_id)


    if request.POST:
        form = ConfirmFoundForm(request.POST)
        if form.is_valid():

            send_mail_to_user('Perro perdido publicado en Oh My Dog!', 
                      f"""Una persona cree haber encontrado a {post.name} \n\nEstos son sus datos: \nEmail: {form.cleaned_data["email"]} \nTelefono: {form.cleaned_data["telephone"]} \nMensaje: {form.cleaned_data["description"]} \n\nContactese con él para confirmar o rechazar la solicitud.""", 
                      form.cleaned_data["email"], 
                      [post.author.email])
            
            send_mail_to_user('Perro perdido publicado en Oh My Dog!', 
                      f"""Crees haber encontrado al perro {post.name}, {post.breed}, {post.sex}, en la zona: '{post.zone}' \n\nDebe esperar a que el dueño decida contactarse con usted \n\nEquipo de Oh My Dog! """,
                      "ohmydog@gmail.com", 
                      [form.cleaned_data["email"]])


            return redirect('confirm_found_succeed', post.id)
    else:
        if(request.user.is_authenticated):
            form = ConfirmFoundForm(
                initial={
                    'email' : request.user.email,
                    'telephone' : request.user.telephone,
                }
            )
        else:
            form = ConfirmFoundForm()

    context = {
        'confirm_found_form' : form,
        'post_id': post.id,
    }
        
    return render(request, 'confirm_found_form.html', context)




def confirm_found_succeed(request, post_id):
    return render(request, 'confirm_found_succeed.html')

