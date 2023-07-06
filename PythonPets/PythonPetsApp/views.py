from django.shortcuts import render
from django.template import loader


def home (request):
    return render(request, "home.html")

def nosotros (request):
    return render(request, "nosotros.html")

def catalogo (request):
    return render(request, "catalogo.html")

def contacto (request):
    return render(request, "contacto.html")