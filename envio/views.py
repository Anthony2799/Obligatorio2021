from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
import datetime

from envio.forms import EnvioForm  




def Alta(request):
    return render(request,)


def home(request):
    return render(request,'home.html')

def Alta_envio(request):
    
    return render(request,'RegistroEnvio.html')


def alta_envio(request): 
    form = EnvioForm(request.POST)
    if request.method == 'POST':
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
        print("Paso para guardar") 
    else:
        print("pase por el else")   
    
    return render(request,'RegistroEnvio.html')

  

    
 