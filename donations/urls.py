from django.urls import path
from . import views

urlpatterns = [

    path("", views.campaigns_list, name='campaigns'),
    path("publish_campaign/", views.publish_campaign, name='campaign_form'),
    path("publish_campaign/done/", views.publish_campaign_succeed, name='campaign_form_succeed')
]