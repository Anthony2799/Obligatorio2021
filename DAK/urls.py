
from django.contrib import admin
from django.urls import path , include
from usuario import views as views_usuarios
from envio import views as views_envio
from traking import views as views_traking




urlpatterns = [
    path('admin/', admin.site.urls),
    path('AltaEnvio/',views_envio.Alta_envio, name="AltaEnvio"),
    path("RegistroTraking/", views_traking.registro_traking , name="RegistroTriaking"),
    path("home/",views_envio.home,name= "home"),
    path("AltaCliente/",views_usuarios.altacliente),
    path('altaEnvio/',views_envio.alta_envio, name="altaEnvio"),
]
