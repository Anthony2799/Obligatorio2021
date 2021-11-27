from django import forms

from django.shortcuts import render, redirect
from usuario.forms import ClienteForm     


from .models import Perfil_cliente
# Create usuario
from django.views.generic import CreateView, UpdateView, ListView

def altacliente(request):
    if request.method == 'GET':
        form = ClienteForm()
        contexto = {
                'form':form
        } 
    else:
        form = ClienteForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
    
    return render(request,'RegistroClientes.html',contexto)        


class addCLiente(CreateView):
    model = Perfil_cliente
    template_name = 'RegistroClientes.html'
    fields = '__all__'
    success_url = '/Alta'