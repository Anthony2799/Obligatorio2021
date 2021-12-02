
from django.contrib import admin
from django.urls import path , include
from usuario import views as views_usuarios
from envio import views as views_envio
from traking import views as views_traking




urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('AltaEnvio/',views_envio.altaEnvio, name="RegistroEnvio"),
    path("RegistroTraking/", views_traking.registro_traking , name="RegistroTriaking"),
    path("home/",views_envio.altaEnvio,name= "home"),
    path("AltaCliente/",views_usuarios.altaCliente,name="RegistroClientes"),
     path("AltaCliente/",views_usuarios.altaEntidad,name="RegistroEntidad"),
      path("AltaCliente/",views_usuarios.altaEmpresa,name="RegistroEmpresa")
=======
    path('AltaEnvio/',views_envio.Alta_envio, name="AltaEnvio"),
    path("RegistroTraking/", views_traking.registro_traking , name="RegistroTriaking"),
    path("home/",views_envio.home,name= "home"),
    path("AltaCliente/",views_usuarios.altacliente),
    path('altaEnvio/',views_envio.alta_envio, name="altaEnvio"),
>>>>>>> e97f756a4114ca67bf14b64fb3cf3c1cbcb241f6
]
