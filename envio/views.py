from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from envio.clases.group import Grupo
from envio.forms import EnvioForm
from usuario.models import Entidad




def alta_envio(request):
    if request.method == 'POST':
        form = EnvioForm(request.POST)
        if form.is_valid:
            form.save()
        
        for i in Entidad:
            if form.numero_entidad == i.numero_entidad:   
                if i.numero_grupo == 'P': 
                    form.precio= Grupo.execute(form.peso)
                elif i.numero_grupo == 'DP': 
                    form.precio= Grupo.execute(form.peso, form.distancia)
                else:
                    form.precio= Grupo.execute()
                
        return redirect('RegistroEnvio.html')
    else:
        form = EnvioForm()
    return render(request,'RegistroEnvio.html',{'form':form})

def homeREturn(request):
    return render(request, 'home.html')
 