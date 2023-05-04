# pages/views.py
from django.shortcuts import render
#from django.views.generic import TemplateView

#Creo clases para las paginas
# class HomePageView(TemplateView):       #TemplateView posee toda la lógica para mostrar el template
#     template_name = 'home.html'         #especifico el nombre del archivo con el template

# class ProfilePageView(TemplateView):
#     template_name = 'profile.html'

def home_view(request):
    return render(request, "home.html", {})