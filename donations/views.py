from django.shortcuts import render
from .models import Campaign

# Create your views here.


def campaigns_list(request):

    campaigns = Campaign.objects.all()
    
    return render(request, 'campaigns_list.html', {'campaigns': campaigns})