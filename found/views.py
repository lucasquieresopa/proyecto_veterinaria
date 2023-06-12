from django.shortcuts import render, redirect
from accounts.models import CustomUser

from .filtros_found import OrderFilter
from .models import FoundPost
from .forms import FoundPostForm, FoundPostModificationForm, ConfirmDeliveredForm
from django.contrib.auth.decorators import login_required
from pages.email_sending import send_mail_to_user

from .filtros_found import OrderFilter

# Create your views here.

@login_required
def found_post_form_view(request):
    user = request.user
    
    if request.POST:
        form = FoundPostForm(request.POST, request.FILES, user=user)

        if form.is_valid():
            found_post = form.save(commit=False)
            found_post.author = user
            found_post.save()
            return redirect('found_post_form_succeed')  
        else:
            context = {
                'found_post_form' : form
            }
    else:
        form = FoundPostForm(user=user)
        context = {
                'found_post_form' : form
                }
        
    return render(request, 'found_post_form.html', context)

@login_required
def found_post_form_succeed(request):
    return render(request, 'found_post_form_succeed.html')


def found_posts_list(request):
    """activa el template que muestra las publicaciones de perdidos excluyendo las del usuario"""
    found_posts = FoundPost.objects.all().order_by('-publication_date', 'was_delivered')


    post_filter = OrderFilter(request.GET, queryset=found_posts)
    found_posts = post_filter.qs

    context = {
        'posts': found_posts,
        'actual_user_id': request.user.id,
        'filter': post_filter,
    }

    return render(request, 'found_post_list.html', context)


@login_required
def client_found_posts_list(request):

    client = CustomUser.objects.get(pk=request.user.id)
    client_found_posts = client.foundpost_set.all().order_by('-publication_date', 'was_delivered')

    post_filter = OrderFilter(request.GET, queryset=client_found_posts)
    client_found_posts = post_filter.qs

    context = {
        'posts': client_found_posts,
        'filter': post_filter,
    }

    return render(request, 'client_found_post_list.html', context)


@login_required
def found_post_modification(request, post_id):

    post = FoundPost.objects.get(id=post_id)

    if request.POST:
        form = FoundPostModificationForm(request.POST, request.FILES, instance=post, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('found_post_modification_succeed')
    else:
        form = FoundPostModificationForm(
            initial = {
                'description': post.description,
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
        form = FoundPostModificationForm(instance=post, user=request.user)
    
    context = {
        'found_post_modification_form': form,
    }

    return render(request, 'found_post_modification_form.html', context)

@login_required
def found_post_modification_succeed(request):
    return render(request, 'found_post_modification_succeed.html')



def delete_found_post(request, post_id):
    """borrado de post en la pestaña de posts propios"""
    post = FoundPost.objects.get(pk=post_id)
    post.delete()
    return redirect('client_found_posts')


def delete_found_post_from_general(request, post_id):
    """borrado de post en la pestaña con todas las publicaciones"""
    post = FoundPost.objects.get(pk=post_id)
    post.delete()
    return redirect('found_posts')


def mark_as_delivered(request, post_id):
    post = FoundPost.objects.get(pk=post_id)
    post.was_delivered = True
    post.save()
    return redirect('client_found_posts')


def mark_as_delivered_from_general(request, post_id):
    post = FoundPost.objects.get(pk=post_id)
    post.was_delivered = True
    post.save()
    return redirect('found_posts')



def confirm_delivered(request, post_id):
    post = FoundPost.objects.get(pk=post_id)


    if request.POST:
        form = ConfirmDeliveredForm(request.POST)
        if form.is_valid():

            send_mail_to_user('Perro encontrado publicado en Oh My Dog!', 
                      f"""Una persona cree que es su perro {post.description}, \n\nEstos son sus datos: \nEmail: {form.cleaned_data["email"]} \nTelefono: {form.cleaned_data["telephone"]} \nMensaje: {form.cleaned_data["description"]} \n\nContactese con él para confirmar o rechazar la solicitud.""", 
                      form.cleaned_data["email"], 
                      [post.author.email])
            
            send_mail_to_user('Perro encontrado publicado en Oh My Dog!', 
                      f"""Crees que es su perro al perro {post.description}, {post.breed}, {post.sex}, en la zona: '{post.zone}' \n\nDebe esperar a que el dueño decida contactarse con usted \n\nEquipo de Oh My Dog! """,
                      "ohmydog@gmail.com", 
                      [form.cleaned_data["email"]])


            return redirect('confirm_delivered_succeed', post.id)
    else:
        form = ConfirmDeliveredForm()

    context = {
        'confirm_delivered_form' : form,
        'post_id': post.id,
    }
        
    return render(request, 'confirm_delivered_form.html', context)




def confirm_delivered_succeed(request, post_id):
    return render(request, 'confirm_delivered_succeed.html')

