from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('found_post_form/', views.found_post_form_view, name= 'found_post_form'),
    path('found_post_form/published/', views.found_post_form_succeed , name= 'found_post_form_succeed'),
    path('foundposts/', views.found_posts_list, name='found_posts'),
    path('foundposts/own_posts/', views.client_found_posts_list, name='client_found_posts'),
    path('foundposts/post_modification/<post_id>', views.found_post_modification, name='found_post_modification'),
    path('foundposts/post_modification/done/', views.found_post_modification_succeed, name='found_post_modification_succeed'),
    path('foundposts/delete_lost_post/<post_id>', views.delete_found_post, name='delete_found_post'),
    path('foundposts/delete_lost_post_from_general/<post_id>', views.delete_found_post_from_general, name='delete_found_post_from_general'),
    path('foundposts/delivered/<post_id>', views.mark_as_delivered, name='mark_as_delivered'),
    path('foundposts/delivered_from_general/<post_id>', views.mark_as_delivered, name='mark_as_delivered_from_general'),
    path('foundposts/confirm_delivered/<post_id>/', views.confirm_delivered, name='confirm_delivered'),
    path('posts/confirm_delivered/<post_id>/done/', views.confirm_delivered_succeed, name='confirm_delivered_succeed'),


] 