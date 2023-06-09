from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('lost_post_form/', views.lost_post_form_view, name= 'lost_post_form'),
    path('lost_post_form/published/', views.lost_post_form_succeed , name= 'lost_post_form_succeed'),
    path('lostposts/', views.lost_posts_list, name='lost_posts'),
    path('lostposts/own_posts/', views.client_lost_posts_list, name='client_lost_posts'),
    path('lostposts/post_modification/<post_id>', views.lost_post_modification, name='lost_post_modification'),
    path('lostposts/post_modification/done/', views.lost_post_modification_succeed, name='lost_post_modification_succeed'),
    path('lostposts/delete_lost_post/<post_id>', views.delete_lost_post, name='delete_lost_post'),
    path('lostposts/delete_lost_post_from_general/<post_id>', views.delete_lost_post_from_general, name='delete_lost_post_from_general'),
    path('lostposts/found/<post_id>', views.mark_as_found, name='mark_as_found'),
    path('lostposts/found_from_general/<post_id>', views.mark_as_found, name='mark_as_found_from_general'),
    path('lostposts/confirm_found/<post_id>/', views.confirm_found, name='confirm_found'),
    path('posts/confirm_found/<post_id>/done/', views.confirm_found_succeed, name='confirm_found_succeed'),


] 