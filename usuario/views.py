from django import forms
from django.shortcuts import render, redirect  
from usuario.forms import usuarioForm    
from usuario.models import Entidad  
from django.http import HttpResponseRedirect
from .forms import usuarioForm

import pdb
# Create usuario
def get_name(request):  
    pdb.set_trace()
    if request.method == 'POST':
        form = usuarioForm(request.POST)
        if form.is_valid():
            pdb.set_trace()
            return HttpResponseRedirect('home.html')
    else:
        form = usuarioForm()
        pdb.set_trace()
        return render(request,'RegistroCliente.html',{'form':form}) 
    
#def show(request):
#    usuarios = Entidad.objects.all()
#    return render(request,'show.html',{'usuarios':usuarios})

def cliR(request):
    pdb.set_trace()
    return render("RegistroClentesl.html", 'helllo word')