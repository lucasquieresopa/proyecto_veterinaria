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
from accounts.views import user_registration_view, logout_view, login_view, account_modif_view, password_reset_view
#from pages.views import HomePageView, ProfilePageView
from pages.views import home_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),         #apunta a la app de auth 
    # path('accounts/', include('accounts.urls')), # apunta a la app accounts
    #                                             #el orden de las instrucciones importa. Primero busca en 
    #                                             # auth, y si no encuentra, busca en accounts
    #path('', TemplateView.as_view(template_name='home.html'), name='home'), # 
    #path("", HomePageView.as_view(), name="home"),      #cuando usamos Class-Based Views se agrega as_view()
    #path("", include("pages.urls")),        #apunta el URL existente a la app pages
    #path("profile/", ProfilePageView.as_view(), name="profile"),
    path("", home_view, name="home"),
    path("login/", login_view, name="login"),
    path('client-registration/', user_registration_view, name='client-registration'),
    path('logout/', logout_view, name="logout"),
    path('modif/', account_modif_view, name='account-modif'),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/', password_reset_view, name='password-reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'), 
]
