from django.contrib import admin
from PythonPetsApp.models import Articulos

class ArticulosAdmin(admin.ModelAdmin):
    list_display=("codigo","nombre","seccion","precio","imagen")
    search_fields=("nombre","seccion")
    list_filter=("codigo","nombre","seccion")

admin.site.register(Articulos,ArticulosAdmin)