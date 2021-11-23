from django.shortcuts import render
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
import datetime

from DAK.usuario.models import Entidad





def alta_envio(request):
    
    return render(request,'RegistroClientes.html')

  
def agregar_cliente(request):
    context={}
    if request.method =='POST':
        estado=False 
        cont= Entidad()
        cont.numero_entidad = request.POST['']
        cont.email=request.POST['email']
        cont.comment=request.POST['comment']
        cont.save()  

    estado=True
  
    context={"estado":estado}
    return render(request,'web/contact.html',context)
    estado=False 

    cont= Contact()
    cont.name=request.POST['name']
    cont.email=request.POST['email']
    cont.comment=request.POST['comment']
  
    cont.save()
    estado=True
  
    context={"estado":estado}

    
  
 return render(request,'web/contact.html',context)