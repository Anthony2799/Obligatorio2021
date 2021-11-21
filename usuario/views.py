from django import forms
from django.shortcuts import render, redirect  
from usuario.forms import usuarioForm    
from usuario.models import Entidad  
# Create usuario
def crerUsuario(request):
    if request.method == "POST":
        form = usuarioForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
        else:
            form = usuarioForm()
            return render(request, 'index.html',{'form':form})

def show(request):
    usuarios = Entidad.objects.all()
    return render(request,"show.html",{'usuarios':usuarios})