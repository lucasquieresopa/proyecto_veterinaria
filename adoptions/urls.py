from django.urls import path
from . import views

urlpatterns = [
    path(
        'adoption_post_form/', 
         views.adoption_post_form_view, 
         name= 'adoption_post_form'),
    path(
        'adoption_post_form/published/', 
        views.adoption_post_form_succeed, 
        name= 'adoption_post_form_succeed'),

    path(
        'posts/', 
        views.adoption_posts_list, 
        name='adoption_posts'),
    path(
        'posts/own_posts/', 
        views.client_adoption_posts_list, 
        name='client_adoption_posts'),
    path(
        'posts/post_modification/<post_id>', 
        views.adoption_post_modification, 
        name='adoption_post_modification'),
    path(
        'posts/post_modification/done/', 
        views.adoption_post_modification_succeed, 
        name='adoption_post_modification_succeed'),
    path(
        'posts/delete_adoption_post/<post_id>', 
        views.delete_adoption_post, 
        name='delete_adoption_post'),
    path(
        'posts/delete_adoption_post_from_general/<post_id>', 
        views.delete_adoption_post_from_general, 
        name='delete_adoption_post_from_general'),
    path(
        'posts/adopted/<post_id>',
        views.mark_as_adopted,
        name='mark_as_adopted'),
    path(
        'posts/adopted_from_general/<post_id>',
        views.mark_as_adopted,
        name='mark_as_adopted_from_general'),
    path(
        'posts/confirm_adoption/<post_id>/',
        views.confirm_adoption,
        name='confirm_adoption'
    ),
    path(
        'posts/confirm_adoption/<post_id>/done/',
        views.confirm_adoption_succeed,
        name='confirm_adoption_succeed'
    ),
    

]