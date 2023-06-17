from django.urls import path
from . import views

urlpatterns = [

    path("", views.campaigns_list, name='campaigns'),
]