from django.conf import settings
from django.conf.urls.static import static
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

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)