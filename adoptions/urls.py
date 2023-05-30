from django.urls import path
from . import views

urlpatterns = [
    #path('adoption_posts', views.dog_registration_view, name= 'adoption_posts'),
    path('adoption_post_form/', views.adoption_post_form_view, name= 'adoption_post_form'),
    path('adoption_post_form/published/', views.adoption_post_form_succeed, name= 'adoption_post_form_succeed'),

]