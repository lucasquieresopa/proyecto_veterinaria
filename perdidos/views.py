from django.shortcuts import render, redirect


from .forms import LostPostForm
from django.contrib.auth.decorators import login_required

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

