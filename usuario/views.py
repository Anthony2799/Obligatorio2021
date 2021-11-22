from django import forms
from django.shortcuts import render, redirect  
from usuario.forms import usuarioForm    
from usuario.models import Entidad  
from django.http import HttpResponse
import pdb
# Create usuario
def emp(request):
   # pdb.set_trace()
    pdb.set_trace()
    if request.method == "POST":
        pdb.set_trace()
        form = usuarioForm(request.POST)
        if form.is_valid():
            try:
                pdb.set_trace()
                form.save()
                return redirect('/show')
            except:
                pass
        else:
            form = usuarioForm()
            pdb.set_trace()
            return render(request,'index.html',{'form':form})
    pdb.set_trace()
    
def show(request):

    usuarios = Entidad.objects.all()
    return render(request,'show.html',{'usuarios':usuarios})

def cliR(request):
    pdb.set_trace()
    return render("RegistroClentesl.html", 'helllo word')