from datetime import date
import datetime
from django.shortcuts import redirect, render
from .models import Campaign, Discount
from .forms import CampaignForm, CampaignModificationForm
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from pages.email_sending import send_mail_to_user

import stripe

stripe.api_key = "sk_test_51NL2vMF7u9x15zyl0VVAsEpA72PT0Y5Jn1ZCtVex9yvIe1dB8NxtTKh2LzeomZWZUQ9xuHbWBoAG2H1UwEmxcCnM00lLca3xpU"

# Create your views here.


def campaigns_list(request):

    campaigns = Campaign.objects.filter(target_date__gte=date.today())

    context = {
        'campaigns': campaigns,
        'actual_user_id': request.user.id,
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







def donate(request, campaign_id):
    return render(request, 'donate.html', {'campaign_id': campaign_id})


def charge(request, campaign_id):

    
    if request.method == "POST":

        email_entered = request.POST['email']
        amount = int(request.POST['amount'])

        #creo un "cliente" de Stripe
        customer = stripe.Customer.create(
            email=email_entered,
            source=request.POST['stripeToken'],
        )

        #creo un "pago" de Stripe
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency="usd",
            description="Donación",
        )

        #sumo el dinero de la donacion a la campaña
        campaign = Campaign.objects.get(pk=campaign_id)
        campaign.actual_money += amount
        campaign.save()

        #aplico descuento al cliente o no cliente
        if(CustomUser.objects.filter(email=email_entered).exists()):
            user = CustomUser.objects.get(email=email_entered)
            if(user.is_veterinario):
                send_mail_to_user('Donación realizada', 
                      f"""Su donación de ${amount} a la causa "{campaign.campaign_name}" fue recibida.¡Gracias por su colaboración!\nEquipo de Oh My Dog!""", 
                      "ohmydog@gmail.com", 
                      [email_entered])
            else:
                if(user.has_discount == False):
                    user.has_discount = True
                    user.save()
                send_mail_to_user('Donación realizada', 
                      f"""Su donación de ${amount} a la causa "{campaign.campaign_name}" fue recibida. \nRecibirá un descuento del 10% en su próxima visita (si no tiene un descuento pendiente).\n¡Gracias por su colaboración!\nEquipo de Oh My Dog!""", 
                      "ohmydog@gmail.com", 
                      [email_entered])
                
        else:
            if(not Discount.objects.filter(email=email_entered).exists()):
                discount = Discount.objects.create(email=email_entered)
                discount.save()
                send_mail_to_user('Donación realizada', 
                      f"""Su donación de ${amount} a la causa "{campaign.campaign_name}" fue recibida. \nSi usted no es cliente aún, recibirá un descuento del 10% en su próxima visita si se asocia a la veterinaria.\n¡Gracias por su colaboración!\nEquipo de Oh My Dog!""", 
                      "ohmydog@gmail.com", 
                      [email_entered])


        

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