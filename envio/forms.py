from django import forms
from django.forms import widgets
from .models import Envio

class EnvioForm(forms.ModelForm):
    class Meta:
        model = Envio 
        fields = [
            'numero_entidad',
            'documento_usuario',
            'peso_paquete',
            'Latitud',
            'Longitud',
            'costo',
            'estado',
        ]
        labels = {
            'numero_entidad'    : 'Entidad',
            'documento_usuario' : 'Cliente',
            'peso_paquete'      : 'Peso paquete',
            'Latitud'           : 'Latitud',
            'Longitud'          : 'Longitud',
            'costo'             : 'costo',
            'estado'            : 'estado',
        }
        widgets = {
            'numero_entidad'     : forms.Select(attrs={'class':'input is-normal'}),
            'documento_usuario'  : forms.Select(attrs={'class':'input is-normal'}),
            'peso_paquete'       : forms.NumberInput(attrs={'class':'input is-normal','step':0.5}),
            'Latitud'            : forms.TextInput(attrs={'class':'input is-normal','id':'lat'}),
            'Longitud'           : forms.TextInput(attrs={'class':'input is-normal','id':'lng'}),
            'costo'              : forms.TextInput(attrs={'class':'input is-normal'}),
            'estado'             : forms.TextInput(attrs={'class':'input is-normal'}),
        }