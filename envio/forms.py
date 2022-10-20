from django import forms
from django.db.models import fields
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
            'estado',
            'distancia',
        ]
        labels = {
            #'numero_entidad'    : 'Entidad',
            'documento_usuario' : 'Cliente',
            'peso_paquete'      : 'Peso paquete',
            'Latitud'           : 'Latitud',
            'Longitud'          : 'Longitud',
            'estado'            : 'estado',
            'distancia'         : 'distancia',
        }
        widgets = {

            'documento_usuario'  : forms.Select(attrs={'class':'input is-normal'}),
            'peso_paquete'       : forms.NumberInput(attrs={'class':'input is-normal','step':0.5}),
            'Latitud'            : forms.TextInput(attrs={'class':'input is-normal','id':'lat'}),
            'Longitud'           : forms.TextInput(attrs={'class':'input is-normal','id':'lng'}),
            'estado'             : forms.TextInput(attrs={'class':'input is-normal'}),
            'distancia': forms.HiddenInput(attrs={'class': 'input is-normal'}),

            
        }


class PagoForm(forms.Form):
    
    OPTIONS = (
                ("Efectivo", "Efectivo"),
                ("Debito", "Debito"),
                ("Cretido", "Cretido"),
                ("Mercado_pago", "Mercado_pago"),
                )
    metodo = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OPTIONS),
    precio            = forms.CharField( max_length=30,required=False),
    nro_tarjeta       = forms.TextInput(attrs={'class':'input is-normal'}),
    cuotas            = forms.TextInput(attrs={'class':'input is-normal'}),