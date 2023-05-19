from django.urls import path
from . import views

urlpatterns = [
    path('dog_registration/<pk>', views.dog_registration_view, name= 'dog_registration'),
    path('dog_profile/<pk>', views.dog_profile_view, name='dog_profile'),
]