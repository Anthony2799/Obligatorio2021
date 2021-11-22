from django import forms
from django.db.models import fields
from usuario.models import Entidad
class usuarioForm(forms.ModelForm):
    class Meta:
        model = Entidad
        fields = "__all__"