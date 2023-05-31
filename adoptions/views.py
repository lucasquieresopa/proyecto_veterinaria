from django.shortcuts import redirect, render

from adoptions.models import AdoptionPost
from .forms import AdoptionPostForm
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
                                                        'posts': adoptions_posts
                                                    }
    )