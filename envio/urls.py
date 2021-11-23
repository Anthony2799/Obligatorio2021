from django.urls import path
from .views import alta_envio , agregar_cliente

urlpatterns = [
    path('AltaEnvio/',alta_envio),
    path('alta_cliente/',agregar_cliente)
]

