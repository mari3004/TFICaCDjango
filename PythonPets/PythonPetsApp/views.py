from django.shortcuts import render
from PythonPetsApp.forms import FormularioContacto
from .models import Articulos


def home (request):
    return render(request, "index.html")

def nosotros (request):
    return render(request, "nosotros.html")

def catalogo (request):
    articulos=Articulos.objects.all()
    return render(request, "catalogo.html",{"articulos":articulos})

def contacto (request):
    return render(request, "contacto.html")

# def contactanos (request):
#     if request.method == "POST":
#         miFormulario=FormularioContacto(request.POST)
#         if miFormulario.is_valid():
#             infForm=miFormulario.cleaned_data
#             return render(request, "home.html")
#         else:
#             miFormulario=FormularioContacto()
#         return render(request, "contacto.html", {"form":miFormulario})