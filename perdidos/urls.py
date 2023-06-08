from django.urls import path
from . import views

urlpatterns = [
    path('lost_post_form/', views.lost_post_form_view, name= 'lost_form_post')





]