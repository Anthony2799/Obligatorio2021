from django import forms
from .models import Perfil_cliente 


class ClienteForm(forms.ModelForm):
        class Meta:
            model = Perfil_cliente
            fields = '__all__' 