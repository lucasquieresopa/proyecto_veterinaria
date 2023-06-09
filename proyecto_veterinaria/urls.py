"""
URL configuration for proyecto_veterinaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# proyecto_veterinaria/urls.py   (proyecto_veterinaria - config - django_project son lo mismo en la guia)
from django.contrib import admin
from django.urls import path, include
#from django.views.generic.base import TemplateView 
#from accounts.views import user_registration_view, logout_view, login_view, account_modif_view, password_reset_view, ChangePasswordView
#from pages.views import HomePageView, ProfilePageView
#from pages.views import home_view
from django.contrib.auth import views as auth_views
#from pages.views import home2
from django import urls 
from accounts.views import login_view
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('pages.urls')),

    path("login/", login_view, name="login"),
    path('accounts/', include('accounts.urls')),
    path("dogs/", include('dogs.urls')),
    path("turnos/", include('shifts.urls')),
    path("adoptions/", include('adoptions.urls')),
    path("perdidos/", include('perdidos.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

