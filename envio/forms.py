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
            #'costo',
            # 'documento_destinatario',
            'estado',
        ]
        labels = {
            #'numero_entidad'    : 'Entidad',
            'documento_usuario' : 'Cliente',
            'peso_paquete'      : 'Peso paquete',
            'Latitud'           : 'Latitud',
            'Longitud'          : 'Longitud',
            #'costo'             : 'costo',
            # 'documento_destinatario': 'Documento destinatario',
            'estado'            : 'estado',
            'distancia'         : 'distancia',
        }
        widgets = {
            #'numero_entidad'     : forms.Select(attrs={'class':'input is-normal'}),
            'documento_usuario'  : forms.Select(attrs={'class':'input is-normal'}),
            'peso_paquete'       : forms.NumberInput(attrs={'class':'input is-normal','step':0.5}),
            'Latitud'            : forms.TextInput(attrs={'class':'input is-normal','id':'lat'}),
            'Longitud'           : forms.TextInput(attrs={'class':'input is-normal','id':'lng'}),
            #'costo'              : forms.TextInput(attrs={'class':'input is-normal'}),
            #'documento_destinatario': forms.Select(attrs={'class': 'input is-normal'}),
            'estado'             : forms.TextInput(attrs={'class':'input is-normal'}),
            
        }


class PagoForm(forms.Form):
    nro_envio         = forms.TextInput(attrs={'readonly':'readonly'}),
    OPTIONS = (
                ("Efectivo", "Efectivo"),
                ("Debito", "Debito"),
                ("Cretido", "Cretido"),
                )
    metodo = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=OPTIONS),
    precio            = forms.CharField( max_length=30,required=False),
    nro_tarjeta       = forms.TextInput(attrs={'class':'input is-normal'}),
    cuotas            = forms.TextInput(attrs={'class':'input is-normal'}),