from django.urls import path
from . import views

urlpatterns = [
    path('', views.guards_list, name="guards_list"),
    path('guards_form/', views.guard_registration_view, name='guard_form'),

    path(
        'guard_succeed/',
        views.guard_register_succeed,
        name="guard_succeed"
    ),
    path(
        'guard_modification/<guard_id>', 
        views.guard_register_modification, 
        name='guard_register_modification'),
    path(
        'guard_modification/done/', 
        views.guard_register_modification_succeed, 
        name='guard_register_modification_succeed'),

]