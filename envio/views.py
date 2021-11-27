from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
import datetime

from usuario.models import Perfil_cliente
from usuario.models import Entidad  



def Alta(request):
    return render(request,)


def home(request):
    return render(request,'home.html')

def alta_envio(request):
    
    return render(request,'RegistroEnvio.html')

  

    
 