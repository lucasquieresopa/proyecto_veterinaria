# pages/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def homePageView(request):
    return HttpResponse("Hola mundo")

#Creo clases para las paginas
class HomePageView(TemplateView):       #TemplateView posee toda la lógica para mostrar el template
    template_name = 'home.html'         #especifico el nombre del archivo con el template

class ProfilePageView(TemplateView):
    template_name = 'profile.html'
