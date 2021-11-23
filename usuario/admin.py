from django.contrib import admin
from .models import Perfil_cliente
# Register your models here.

@admin.register(Perfil_cliente)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('entidad_usuario','nombre_usuario','apellido_usuario','documento_usuario','fecha_creado','fecha_modficado')
    search_fields = ('nombre_usuario','documento_usuario')

