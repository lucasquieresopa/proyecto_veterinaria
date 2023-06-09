from django.shortcuts import render, redirect
from datetime import date
from email.message import EmailMessage
from accounts.models import CustomUser

from perdidos.models import LostPost
from .forms import LostPostForm, LostPostModificationForm, ConfirmLostForm 
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from pages.email_sending import send_mail_to_user
from .filters import OrderFilter
# Create your views here.

@login_required
def lost_post_form_view(request):
    user = request.user
    
    if request.POST:
        form = LostPostForm(request.POST, user=user)

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
def lost_post_form_succeed(request):
    return render(request, 'lost_post_form_succeed.html')

def lost_posts_list(request):
    """activa el template que muestra las publicaciones de adopcion excluyendo las del usuario"""
    lost_posts = LostPost.objects.all().order_by('-publication_date', 'was_found')


    post_filter = OrderFilter(request.GET, queryset=lost_posts)
    lost_posts = post_filter.qs

    context = {
        'posts': lost_posts,
        'actual_user_id': request.user.id,
        'filter': post_filter,
    }

    return render(request, 'lost_posts_list.html', context)

@login_required
def client_lost_posts_list(request):

    client = CustomUser.objects.get(pk=request.user.id)
    client_lost_posts = client.lostpost_set.all().order_by('-publication_date', 'was_found')

    post_filter = OrderFilter(request.GET, queryset=client_adoption_posts)
    client_lost_posts = post_filter.qs

    context = {
        'posts': client_lost_posts,
        'filter': post_filter,
    }

    return render(request, 'client_lost_posts_list.html', context)

@login_required
def lost_post_modification(request, post_id):

    post = LostPost.objects.get(id=post_id)

    if request.POST:
        form = LostPostModificationForm(request.POST, instance=post, user=request.user)
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
                'zone': post.zone,
                'description': post.description,
                
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
    post.is_found = True
    post.save()
    return redirect('lost_posts')

def confirm_lost(request, post_id):
    post = LostPost.objects.get(pk=post_id)


    if request.POST:
        form = ConfirmLostForm(request.POST)
        if form.is_valid():

            send_mail_to_user('Solicitud de perro encontrado en Oh My Dog!', 
                      f"""Un cliente de Oh My Dog ha solicitado que ah encontrado su perro de nombre {post.name} \n\nEstos son sus datos: \nEmail: {form.cleaned_data["email"]} \nTelefono: {form.cleaned_data["telephone"]} \nMensaje: {form.cleaned_data["description"]} \n\nContactese con el para confirmar o rechazar la solicitud.""", 
                      form.cleaned_data["email"], 
                      [post.author.email])
            
            send_mail_to_user('Solicitud de perro encontrado en Oh My Dog!', 
                      f"""Has solicitado que ah encontrado el perro {post.name}, {post.breed}, {post.sex}, con descripción: '{post.description}' \n\nDebe esperar a que el dueño decida contactarse con usted \n\nEquipo de Oh My Dog! """,
                      "ohmydog@gmail.com", 
                      [form.cleaned_data["email"]])


            return redirect('confirm_lost_succeed', post.id)
    else:
        form = ConfirmLostForm()

    context = {
        'confirm_lost_form' : form,
        'post_id': post.id,
    }
        
    return render(request, 'confirm_lost_form.html', context)

def confirm_lost_succeed(request, post_id):
    return render(request, 'confirm_lost_succeed.html')






