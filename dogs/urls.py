from django.urls import path
from . import views

urlpatterns = [
    path('dog_registration/<pk>', views.dog_registration_view, name= 'dog_registration'),
    path('dog_registration/succeed/<user_owner_id>', views.dog_registration_done, name='dog_registration_succeed'),
    path('dog_profile/<user_owner_id>/<dog_id>', views.dog_profile_view, name='dog_profile'),
    path('dog_modification/<user_owner_id>/<dog_id>', views.dog_modification_view, name='dog_modification'),
    path('dog_modification/succeed/<user_owner_id>/<dog_id>', views.dog_modification_done, name='dog_modification_succeed'),

    path('hide_dog/<dog_id>/', views.hide_or_show_dog, name='hide_or_show_dog'),
    path('hidden_dogs/<user_id>', views.hidden_dogs_view, name="hidden_dogs"),

    path('attention_form/<client_id>/<dog_id>/', views.attention_registration_view, name='attention_form'),
    path('attentions/<client_id>/<dog_id>/', views.attentions_list, name="attentions_list"),

    path('vaccinations/<client_id>/<dog_id>/', views.vaccinations_list, name="vaccinations"),
    path('vaccination_form/<client_id>/<dog_id>/', views.vaccination_registration_view, name='vaccination_form'),

    path(
        'vaccination_succeed/<user_owner_id>/<dog_id>/',
        views.vaccination_register_succeed,
        name="vaccination_succeed"
    ),
    path(
        'attention_succeed/<user_owner_id>/<dog_id>/',
        views.attention_register_succeed,
        name="attention_succeed"
    )

]