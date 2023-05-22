from . import views
from django.urls import path

urlpatterns = [
    path('calendar/', views.views_calendar, name= 'calendar'),
    
    path('', views.booking, name='booking'),
    path('booking-submit/', views.bookingSubmit, name='bookingSubmit'),
    path('user-panel/', views.userPanel, name='userPanel'),
    path('user-update/<int:id>/', views.userUpdate, name='userUpdate'),
    path('user-update-submit/<int:id>/', views.userUpdateSubmit, name='userUpdateSubmit'),
    path('staff-panel/', views.staffPanel, name='staffPanel'),
    path('accept/<id>/', views.confirmAppointment, name='accept'),
    path('reject/<id>/', views.cancelAppointment, name='reject'),
    path('save_appointment/', views.save_appointment, name='save_appointment'),

]