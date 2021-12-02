from django import forms
from django.forms import widgets
from .models import Perfil_cliente ,Entidad,Perfil_empresa


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Perfil_cliente 
        fields = [
            'entidad_usuario',
            'nombre_usuario',
            'apellido_usuario',
            'documento_usuario',
        ]
        labels = {
            'entidad_usuario'   : 'Entidad',
            'nombre_usuario'    : 'Nombre',
            'apellido_usuario'  : 'Apellido',
            'documento_usuario' : 'Documento',
        }
        widgets = {
            'entidad_usuario'    : forms.Select(attrs={'class':'input is-normal'}),
            'nombre_usuario'    : forms.TextInput(attrs={'class':'input is-normal'}),
            'apellido_usuario'  : forms.TextInput(attrs={'class':'input is-normal'}),
            'documento_usuario' : forms.TextInput(attrs={'class':'input is-normal'}),
        }

class EntidadForm(forms.ModelForm):
    class Meta:
        model = Entidad
        fields = [
            'numero_grupo',
            'direccion',
            'email',
            'telefono',
        ]
        labels = {
            'numero_grupo'  : 'Grupo',
            'direccion'     : 'Direccion',
            'email'         : 'E-mail',
            'telefono'      : 'Tel',
            }
        widgets = {
            'numero_grupo'    : forms.Select(attrs={'class':'input is-normal'}),
            'direccion'       : forms.TextInput(attrs={'class':'input is-normal'}),
            'email'           : forms.TextInput(attrs={'class':'input is-normal'}),
            'telefono'        : forms.TextInput(attrs={'class':'input is-normal'}),
            }

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Perfil_empresa
        fields = [
            'entidad_usuario',
            'rut',
            'razon_social',
        ]
        labels = {
            'entidad_usuario'    : 'Entidad',
            'rut'                : 'RUT',
            'razon_social'       : 'Razon Social',
        }
        widgets = {
            'entidad_usuario'    : forms.Select(attrs={'class':'input is-normal'}),
            'rut'                : forms.TextInput(attrs={'class':'input is-normal'}),
            'razon_social'       : forms.TextInput(attrs={'class':'input is-normal'}),   
        }
        
