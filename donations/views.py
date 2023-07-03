from django.shortcuts import redirect, render
from .models import Campaign
from .forms import CampaignForm
from django.contrib.auth.decorators import login_required

import stripe

stripe.api_key = "sk_test_51NL2vMF7u9x15zyl0VVAsEpA72PT0Y5Jn1ZCtVex9yvIe1dB8NxtTKh2LzeomZWZUQ9xuHbWBoAG2H1UwEmxcCnM00lLca3xpU"

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







def donate(request, campaign_id):
    return render(request, 'donate.html', {'campaign_id': campaign_id})


def charge(request, campaign_id):

    if request.method == "POST":

        customer = stripe.Customer.create(
            email=request.POST['email'],
            source=request.POST['stripeToken'],
            
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=500,
            currency="usd",
            #source=request.POST['stripeToken'],
            description="Donación",
        )

        campaign = Campaign.objects.get(pk=campaign_id)
        campaign.actual_money += 500/100
        campaign.save()

    return redirect('donation_succeed')


def donation_succeed(request):
    return render(request, 'donation_succeed.html')




# def calculate_order_amount(items):
#     # Replace this constant with a calculation of the order's amount
#     # Calculate the order total on the server to prevent
#     # people from directly manipulating the amount on the client
#     return 1400


# @app.route('/create-payment-intent', methods=['POST'])
# def create_payment():
#     try:
#         data = json.loads(request.data)
#         # Create a PaymentIntent with the order amount and currency
#         intent = stripe.PaymentIntent.create(
#             amount=calculate_order_amount(data['items']),
#             currency='eur',
#             automatic_payment_methods={
#                 'enabled': True,
#             },
#         )
#         return jsonify({
#             'clientSecret': intent['client_secret']
#         })
#     except Exception as e:
#         return jsonify(error=str(e)), 403