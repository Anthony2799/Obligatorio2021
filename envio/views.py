from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from envio.clases.group import Grupo
from envio.forms import EnvioForm
from usuario.models import Entidad


def homeREturn(request):
    return render(request, 'home.html')

def alta_envio(request):
    if request.method == 'POST':
        form = EnvioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('RegistroEnvio.html')
    else:
        form = EnvioForm()
    return render(request,'RegistroEnvio.html',{'form':form})

def homeREturn(request):
    return render(request, 'home.html')
 