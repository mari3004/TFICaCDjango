from django.shortcuts import render, redirect
from .forms import ArticuloForm
from .models import Articulos
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages

def home (request):
    return render(request, "index.html")

def nosotros (request):
    return render(request, "nosotros.html")

def catalogo (request):
    articulos=Articulos.objects.all()
    return render(request, "catalogo.html",{"articulos":articulos})

def abm (request):
    articulos=Articulos.objects.all()
    return render(request, "inventario/abm.html",{"articulos":articulos})

def crearproducto(request):
    formulario = ArticuloForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('ABM')
    return render(request, 'inventario/crear_producto.html', {'formulario': formulario})


def editarproducto(request, id):
    articulo = Articulos.objects.get(id=id)
    formulario =ArticuloForm(request.POST or None, request.FILES or None, instance=articulo)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Catalogo')
    return render(request, "inventario/editar_producto.html", {'formulario': formulario})

def eliminarproducto(request, id):
    articulo = Articulos.objects.get(id=id)
    articulo.delete()
    return redirect('ABM')

def contacto (request):
    return render(request, "contacto.html")

def login (request):
    return render(request, "login.html")

def registro (request):
#    data = {
#        'form': CustomUserCreationForm()
#    }
#    if request.method == 'POST':
#        formulario = CustomUserCreationForm(data=request.POST)
#        if formulario.is_valid():
#            formulario.save()
#            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
#            login(request, user)
#            messages.sucess(request, "Te has registrado correctamente")
#            return redirect(to='Home')
#        data['form'] = formulario
   return render(request, 'registro.html')

def salir(request):
    logout(request)
    HttpResponse("La sesion se ha cerrado correctamente")
    return redirect("Login")