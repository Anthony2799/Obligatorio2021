from django import forms
from django.db.models import fields
from usuario.models import Entidad
class usuarioForm(forms.Form):
    algo = forms.CharField(label="nombre", max_length=100)