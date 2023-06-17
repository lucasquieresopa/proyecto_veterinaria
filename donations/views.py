from django.shortcuts import redirect, render
from .models import Campaign
from .forms import CampaignForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def campaigns_list(request):

    campaigns = Campaign.objects.all()

    context = {
        'campaigns': campaigns,
        'actual_user_id': request.user.id
    }
    
    return render(request, 'campaigns_list.html', context)



@login_required
def publish_campaign(request):
    user = request.user
    
    if request.POST:
        form = CampaignForm(request.POST, request.FILES, user=user)

        if form.is_valid():
            found_post = form.save(commit=False)
            found_post.author = user
            found_post.save()
            return redirect('campaign_form_succeed')  
        else:
            context = {
                'campaign_form' : form
            }
    else:
        form = CampaignForm(user=user)
        context = {
                'campaign_form' : form
                }
        
    return render(request, 'campaign_form.html', context)


def publish_campaign_succeed(request):
    return render(request, 'campaign_form_succeed.html')