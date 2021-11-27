from django import forms

from django.shortcuts import render, redirect     
from usuario.models import Entidad  
from django.http import HttpResponse
import pdb
from .models import Perfil_cliente
# Create usuario
from django.views.generic import CreateView, UpdateView, ListView
def base_view(request):
    return HttpResponse("ok")

 

class addCLiente(CreateView):
    model = Perfil_cliente
    template_name = 'RegistroClientes.html'
    fields = '__all__'
    success_url = '/Alta'