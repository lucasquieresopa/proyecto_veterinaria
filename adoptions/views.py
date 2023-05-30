from django.shortcuts import redirect, render
from .forms import AdoptionPostForm
from django.contrib.auth.decorators import login_required

@login_required
def adoption_post_form_view(request):
    """definicion del formulario de publicación de adopción"""

    user = request.user
    # if not user.is_authenticated:
    #     return redirect('home')

    if request.POST:
        form = AdoptionPostForm(request.POST)

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
        form = AdoptionPostForm()
        context = {
                'adoption_post_form' : form
                }
        
    return render(request, 'adoption_post_form.html', context)





@login_required
def adoption_post_form_succeed(request):
    return render(request, 'adoption_post_form_succeed.html')
    