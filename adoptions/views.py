from django.shortcuts import redirect, render
from accounts.models import CustomUser

from adoptions.models import AdoptionPost
from .forms import AdoptionPostForm, AdoptionPostModificationForm
from django.contrib.auth.decorators import login_required

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

    adoptions_posts = AdoptionPost.objects.all()

    return render(request, 'adoption_posts_list.html', {
                                                        'posts': adoptions_posts,
                                                       
                                                    }
    )


@login_required
def client_adoption_posts_list(request):

    client = CustomUser.objects.get(pk=request.user.id)
    client_adoption_posts = client.adoptionpost_set.all()

    return render(request, 'client_adoption_posts_list.html', {
                                                                'posts': client_adoption_posts,
          
          
                                                            })
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