from . import views
from django.urls import path

urlpatterns = [
    #path('', views.views_calendar, name= 'calendar'),
    
    path('booking/', views.booking, name='booking'),
    path('booking-submit/', views.bookingSubmit, name='bookingSubmit'),
    path('user-panel/', views.userPanel, name='userPanel'),
    path('user-update/<int:id>/', views.userUpdate, name='userUpdate'),
    path('user-update-submit/<int:id>/', views.userUpdateSubmit, name='userUpdateSubmit'),
    path('staff-panel/', views.staffPanel, name='staffPanel'),
]