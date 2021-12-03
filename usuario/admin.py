from django.contrib import admin
from django.urls.converters import DEFAULT_CONVERTERS

from .models import Perfil_cliente,Perfil_empresa, Perfil_funcionario


admin.site.register(Perfil_funcionario)
admin.site.register(Perfil_cliente)
admin.site.register(Perfil_empresa)


