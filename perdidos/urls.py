from django.urls import path
from . import views

urlpatterns = [
    path('lost_post_form/', views.lost_post_form_view, name= 'lost_post_form'),
     path(
        'lost_post_form/published/', 
        views.lost_post_form_succeed, 
        name= 'lost_post_form_succeed'),

    path(
        'posts/', 
        views.lost_posts_list, 
        name='lost_posts'),
    path(
        'posts/own_posts/', 
        views.client_lost_posts_list, 
        name='client_lost_posts'),
    path(
        'posts/post_modification/<post_id>', 
        views.lost_post_modification, 
        name='lost_post_modification'),
    path(
        'posts/post_modification/done/', 
        views.lost_post_modification_succeed, 
        name='lost_post_modification_succeed'),
    path(
        'posts/delete_lost_post/<post_id>', 
        views.delete_lost_post, 
        name='delete_lost_post'),
    path(
        'posts/delete_lost_post_from_general/<post_id>', 
        views.delete_lost_post_from_general, 
        name='delete_lost_post_from_general'),
    path(
        'posts/lost/<post_id>',
        views.mark_as_found,
        name='mark_as_found'),
    path(
        'posts/found_from_general/<post_id>',
        views.mark_as_found,
        name='mark_as_found_from_general'),
    path(
        'posts/confirm_lost/<post_id>/',
        views.confirm_lost,
        name='confirm_lost'
    ),
    path(
        'posts/confirm_lost/<post_id>/done/',
        views.confirm_lost_succeed,
        name='confirm_lost__succeed'
    ),





]