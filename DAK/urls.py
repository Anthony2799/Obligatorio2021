
from django.contrib import admin
from django.urls import path , include
from usuario import views as views_usuarios
from envio import views as views_envio
from traking import views as views_traking




urlpatterns = [
    path('admin/', admin.site.urls),
    path('AltaEnvio/',views_envio.alta_envio, name="RegistroEnvio"),
    path("RegistroTraking/", views_traking.registro_traking , name="RegistroTriaking"),
    path("",views_envio.homeREturn,name= "home"), 
    path("AltaCliente/",views_usuarios.altaCliente,name="RegistroClientes"),
    path("agregar_entidad/",views_usuarios.altaentidad,name="agregar_entidad"),
    path("pagar/",views_envio.Pagar,name="pagar")
]
