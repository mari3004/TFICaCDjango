from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from PythonPetsApp import views
from .views import *


urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home, name="Home"),
    path('nosotros',views.nosotros, name="Nosotros"),
    path('catalogo',views.catalogo, name="Catalogo"),
    path('contacto',views.contacto, name="Contacto"),
    path('login',views.login, name="Login"),
    path('registro',views.registro, name="Registro"),
    path('salir',views.salir, name="Salir"),
    path('abm',views.abm, name="ABM"),
    path('crearproducto',views.crearproducto, name="crearproducto"),
    path('editarproducto/<int:id>',views.editarproducto, name="editarproducto"),
    path('eeliminarproducto/<int:id>',views.eliminarproducto, name="eliminarproducto"),

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)