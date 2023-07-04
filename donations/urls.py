from django.urls import path
from . import views

urlpatterns = [

    path("", views.campaigns_list, name='campaigns'),
    path("publish_campaign/", views.publish_campaign, name='campaign_form'),
    path("publish_campaign/done/", views.publish_campaign_succeed, name='campaign_form_succeed'),

    path("donate/<campaign_id>", views.donate, name='donate'),
    path("donate/succeed/", views.donation_succeed, name='donation_succeed'),
    #path("donate/error/", views.donation_error, name='donation_error'),
    path("charge/<campaign_id>", views.charge, name='charge'),

    path('campaign_modification/<campaign_id>', views.campaign_modification, name='campaign_modification'),
    path('campaign_modification/done/', views.campaign_modification_succeed, name='campaign_modification_succeed'),
    path('delete_campaign/<campaign_id>', views.delete_campaign, name='delete_campaign'),
    

]