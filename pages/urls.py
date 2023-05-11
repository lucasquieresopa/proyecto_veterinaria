# pages/urls.py
from django.urls import path
from . import views

"""In other words, if the user requests the homepage represented by the empty string "", Django should use the view called homePageView."""

urlpatterns = [
    path("", views.home_view, name="home"),
    
]