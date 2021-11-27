
from django.contrib import admin
from django.urls import path , include
from usuario import views as views_usuarios
from envio import views as views_envio
from traking import views as views_traking




urlpatterns = [
    path('admin/', admin.site.urls),
    path('AltaEnvio/',views_envio.alta_envio, name="RegistroEnvio"),
    #path("Clientes/",include('RegistroClientes.html')),
    path("RegistroTraking/", views_traking.registro_traking , name="RegistroTriaking"),
    path("home/",views_envio.home,name= "home"),
    path("AltaCliente/",views_usuarios.altacliente,name="RegistroCliente")
]
