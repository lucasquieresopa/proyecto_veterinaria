from . import views
from django.urls import path

urlpatterns = [
    path('calendar/<id>/', views.views_calendar, name= 'calendar'),
    
    #path('', views.booking, name='booking'),
    # path('booking-submit/', views.bookingSubmit, name='bookingSubmit'),
    # path('user-panel/', views.userPanel, name='userPanel'),
    # path('user-update/<int:id>/', views.userUpdate, name='userUpdate'),
    # path('user-update-submit/<int:id>/', views.userUpdateSubmit, name='userUpdateSubmit'),
    path('shifts_panel/', views.shifts_panel_view, name='shifts_panel'),
    path('accept/<id>/', views.confirmAppointment, name='accept'),
    path('reject/<id>/', views.cancelAppointment, name='reject'),
    path('save_appointment/<id>/', views.save_appointment, name='save_appointment'),
    # path('save_description/<id>/', views.save_description, name='save_description'),
    # path('desbloquear/<id>/', views.desbloquear, name='desbloquear'),
    path('save_descriptionMandado/<id>/', views.save_descriptionMandado, name='save_descriptionMandado'),

    path(
        'send_confirmation_message/<id>/',
        views.send_confirmation_message_view,
        name='send_confirmation_message',
    ),
    path(
        'send_rejection_message/<id>/',
        views.send_rejection_message_view,
        name='send_rejection_message',
    ),
    path(
        'confirmation_mail_sent/<id>/',
        views.confirmation_mail_sent,
        name='confirmation_mail_sent',
    ),
    path(
        'rejection_mail_sent/<id>/',
        views.rejection_mail_sent,
        name='rejection_mail_sent',
    ),
    path(
        'modificate_action/<id>',
        views.modificate_action,
        name='modificate_action'
    ),
    path(
        'reprogram/<id>',
        views.reprogram_view,
        name='reprogram_view'
    ),
    path(
        'reprogram_mail_sent/<id>/',
        views.reprogram_mail_sent,
        name='reprogram_mail_sent',
    ),
    path(
        'shift_peticion_succeed/',
        views.shift_peticion_succeed,
        name='shift_succeed'
    ),
    path('shifts_panel_user/', views.shifts_panel_user_view, name='shifts_panel_user'),


]