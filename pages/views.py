from django.shortcuts import render

# pages/views.py
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Hola mundo")
