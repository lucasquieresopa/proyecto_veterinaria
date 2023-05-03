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
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),         #apunta a la app de auth 
    path('accounts/', include('accounts.urls')), # apunta a la app accounts
                                                #el orden de las instrucciones importa. Primero busca en 
                                                # auth, y si no encuentra, busca en accounts
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # 
    path("", include("pages.urls")),        #apunta el URL existente a la app pages
]
