from datetime import date
from email.message import EmailMessage
from django.shortcuts import redirect, render
from accounts.models import CustomUser

from adoptions.models import AdoptionPost
from .forms import AdoptionPostForm, AdoptionPostModificationForm, ConfirmAdoptionForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from pages.email_sending import send_mail_to_user

from .filters import OrderFilter

@login_required
def adoption_post_form_view(request):
    """definicion del formulario de publicación de adopción"""

    user = request.user
    # if not user.is_authenticated:
    #     return redirect('home')

    if request.POST:
        form = AdoptionPostForm(request.POST, user=user)

        if form.is_valid():
            adoption_post = form.save(commit=False)
            adoption_post.author = user
            adoption_post.save()
            return redirect('adoption_post_form_succeed')  
        else:
            context = {
                'adoption_post_form' : form
            }
    else:
        form = AdoptionPostForm(user=user)
        context = {
                'adoption_post_form' : form
                }
        
    return render(request, 'adoption_post_form.html', context)



@login_required
def adoption_post_form_succeed(request):
    return render(request, 'adoption_post_form_succeed.html')
    



@login_required
def adoption_posts_list(request):
    """activa el template que muestra las publicaciones de adopcion excluyendo las del usuario"""
    adoption_posts = AdoptionPost.objects.all().order_by('-publication_date', 'is_adopted')


    post_filter = OrderFilter(request.GET, queryset=adoption_posts)
    adoption_posts = post_filter.qs

    context = {
        'posts': adoption_posts,
        'actual_user_id': request.user.id,
        'filter': post_filter,
    }

    return render(request, 'adoption_posts_list.html', context)
    


@login_required
def client_adoption_posts_list(request):

    client = CustomUser.objects.get(pk=request.user.id)
    client_adoption_posts = client.adoptionpost_set.all().order_by('-publication_date')

    post_filter = OrderFilter(request.GET, queryset=client_adoption_posts)
    client_adoption_posts = post_filter.qs

    context = {
        'posts': client_adoption_posts,
        'filter': post_filter,
    }

    return render(request, 'client_adoption_posts_list.html', context)
@login_required
def adoption_post_modification(request, post_id):

    post = AdoptionPost.objects.get(id=post_id)

    if request.POST:
        form = AdoptionPostModificationForm(request.POST, instance=post, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('adoption_post_modification_succeed')
    else:
        form = AdoptionPostModificationForm(
            initial = {
                'name': post.name,
                'age': post.age,
                'sex': post.sex,
                'breed': post.breed,
                'color': post.color,
                'size': post.size,
                'origin': post.origin,
                'description': post.description,
                
            },
            user=request.user,
            instance=post
        )
        form = AdoptionPostModificationForm(instance=post, user=request.user)
    
    context = {
        'adoption_post_modification_form': form,
    }

    return render(request, 'adoption_post_modification_form.html', context)


@login_required
def adoption_post_modification_succeed(request):
    return render(request, 'adoption_post_modification_succeed.html')



def delete_adoption_post(request, post_id):
    post = AdoptionPost.objects.get(pk=post_id)
    post.delete()
    return redirect('client_adoption_posts')


def mark_as_adopted(request, post_id):
    post = AdoptionPost.objects.get(pk=post_id)
    post.is_adopted = True
    post.save()
    return redirect('client_adoption_posts')



def confirm_adoption(request, post_id):
    print(post_id)
    post = AdoptionPost.objects.get(pk=post_id)

    if request.POST:
        form = ConfirmAdoptionForm(request.POST)
        if form.is_valid():

            # asunto = 'Solicitud de adopción en Oh My Dog!'
            # remitente = form.cleaned_data["email"]
            # mensaje = f"""Un cliente de Oh My Dog ha solicitado adoptar a su perro {post.name} \n\nEstos son sus datos: \n Email: {remitente} \nTelefono: {form.cleaned_data["telephone"]} \nMensaje: {form.cleaned_data["description"]} \n\nContactese con el para confirmar o rechazar la solicitud.
            #                     """
            
            # send_mail(asunto, mensaje, remitente, ["megat01e28@gmail.com"])

            send_mail_to_user('Solicitud de adopción en Oh My Dog!', 
                      f"""Un cliente de Oh My Dog ha solicitado adoptar a su perro {post.name} \n\nEstos son sus datos: \nEmail: {form.cleaned_data["email"]} \nTelefono: {form.cleaned_data["telephone"]} \nMensaje: {form.cleaned_data["description"]} \n\nContactese con el para confirmar o rechazar la solicitud.""", 
                      form.cleaned_data["email"], 
                      ["megat01e28@gmail.com"])

            return redirect('confirm_adoption_succeed', post.id)
    else:
        form = ConfirmAdoptionForm()

    context = {
        'confirm_adoption_form' : form,
        'post_id': post.id,
    }
        
    return render(request, 'confirm_adoption_form.html', context)




def confirm_adoption_succeed(request, post_id):
    return render(request, 'confirm_adoption_succeed.html')
