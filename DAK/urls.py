
from django.contrib import admin
from django.urls import path , include
from usuario import views as views_usuarios
from envio import views as views_envio
from traking import views as views_traking




urlpatterns = [
    path('admin/', admin.site.urls),
    path('AltaEnvio/',views_envio.alta_envio, name="RegistroEnvio"),
    path("RegistroTraking/", views_traking.registro_traking , name="RegistroTriaking"),
    # path("home/",'home.html',name= "home"),
    path("AltaCliente/",views_usuarios.altaCliente,name="RegistroClientes"),
    path("AltaCliente/",views_usuarios.altaEntidad,name="RegistroEntidad"),
    path("AltaCliente/",views_usuarios.altaEmpresa,name="RegistroEmpresa")
]
