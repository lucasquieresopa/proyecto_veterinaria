from django.urls import path
from . import views

urlpatterns = [
    path('dog_registration/<pk>', views.dog_registration_view, name= 'dog_registration'),
    path('dog_profile/<user_owner_id>/<dog_id>', views.dog_profile_view, name='dog_profile'),
    path('dog_modification/<user_owner_id>/<dog_id>', views.dog_modification_view, name='dog_modification'),
    path('dog_modification/succeed', views.dog_modification_done, name='dog_modification_succeed'),
]