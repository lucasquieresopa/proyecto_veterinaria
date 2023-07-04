from datetime import date
import datetime
from django.shortcuts import redirect, render
from .models import Campaign
from .forms import CampaignForm, CampaignModificationForm
from django.contrib.auth.decorators import login_required

import stripe

stripe.api_key = "sk_test_51NL2vMF7u9x15zyl0VVAsEpA72PT0Y5Jn1ZCtVex9yvIe1dB8NxtTKh2LzeomZWZUQ9xuHbWBoAG2H1UwEmxcCnM00lLca3xpU"

# Create your views here.


def campaigns_list(request):

    campaigns = Campaign.objects.filter(target_date__gte=date.today())

    context = {
        'campaigns': campaigns,
        'actual_user_id': request.user.id,
        'progress': 45,
    }
    
    return render(request, 'campaigns_list.html', context)

def get_progress(id):
    return 20



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







def donate(request, campaign_id):
    return render(request, 'donate.html', {'campaign_id': campaign_id})


def charge(request, campaign_id):

    if request.method == "POST":

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email=request.POST['email'],
            source=request.POST['stripeToken'],
            
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency="usd",
            #source=request.POST['stripeToken'],
            description="Donación",
        )

        campaign = Campaign.objects.get(pk=campaign_id)
        campaign.actual_money += amount
        campaign.save()

    return redirect('donation_succeed')


def donation_succeed(request):
    return render(request, 'donation_succeed.html')




@login_required
def campaign_modification(request, campaign_id):

    campaign = Campaign.objects.get(id=campaign_id)

    if request.POST:
        form = CampaignModificationForm(request.POST, request.FILES, instance=campaign, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('campaign_modification_succeed')
    else:
        form = CampaignModificationForm(
            initial = {
                'campaign_name': campaign.campaign_name,
                'description': campaign.description,
                'target_date': campaign.target_date,
                'target_money': campaign.target_money,
                
            },
            user=request.user,
            instance=campaign
        )
        form = CampaignModificationForm(instance=campaign, user=request.user)
    
    context = {
        'campaign_modification_form': form,
    }

    return render(request, 'campaign_modification.html', context)


@login_required
def campaign_modification_succeed(request):
    return render(request, 'campaign_modification_succeed.html')



def delete_campaign(request, campaign_id):
    """borrado de post en la pestaña de posts propios"""
    campaign = Campaign.objects.get(pk=campaign_id)
    campaign.delete()
    return redirect('campaigns')