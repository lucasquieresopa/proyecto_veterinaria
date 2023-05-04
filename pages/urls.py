# pages/urls.py
from django.urls import path
from .views import HomePageView
from .views import ProfilePageView

"""In other words, if the user requests the homepage represented by the empty string "", Django should use the view called homePageView."""

urlpatterns = [
    
]