from django import forms
from .models import Articulos

class FormularioContacto(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = '__all__'