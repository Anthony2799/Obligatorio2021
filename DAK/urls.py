"""DAK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuario import views as views_usuarios
from envio import views as views_envio
from traking import views as views_traking



urlpatterns = [
    path('admin/', admin.site.urls),
    path('AltaEnvio/',views_envio.alta_envio, name="RegistroEnvio"),
    path("alta_cliente/",views_envio.agregar_cliente , name="RegistroCliente"),
    path("RegistroTraking/", views_traking.registro_traking , name="RegistroTriaking"),
    path("home/",views_envio.home,name= "home"),
    path("get_name/",views_usuarios.get_name)
]
