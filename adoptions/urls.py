from django.urls import path
from . import views

urlpatterns = [
    path('adoption_post_form/', views.adoption_post_form_view, name= 'adoption_post_form'),
    path('adoption_post_form/published/', views.adoption_post_form_succeed, name= 'adoption_post_form_succeed'),

    path('posts/', views.adoption_posts_list, name='adoption_posts'),
    path('posts/own_posts/', views.client_adoption_posts_list, name='client_adoption_posts'),
    path('posts/post_modification/<post_id>', views.adoption_post_modification, name='adoption_post_modification'),
    path('posts/post_modification/done/', views.adoption_post_modification_succeed, name='adoption_post_modification_succeed'),
    
]