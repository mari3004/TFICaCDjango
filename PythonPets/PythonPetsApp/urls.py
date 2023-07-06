from django.contrib import admin
from django.urls import path
from PythonPetsApp import views


urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home, name="Home"),
    path('nosotros',views.nosotros, name="Nosotros"),
    path('catalogo',views.catalogo, name="Catalogo"),
    path('contacto',views.contacto, name="Contacto"),
]

