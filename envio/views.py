from django.shortcuts import render
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
import datetime

from usuario.models import Perfil_cliente
from usuario.models import Entidad  



def home(request):
    return render(request,'home.html')

def alta_envio(request):
    
    return render(request,'RegistroEnvio.html')

  
def agregar_cliente(request):
    
    if request.method =='POST':
        
        ent = Entidad()
        ent.numero_grupo = 0
        ent.direccion = "casapueblo"
        ent.email = request.POST['email']
        ent.telefono = request.POST['tel']
        ent.save()
         
        cont= Perfil_cliente()
        cont.entidad_usuario = ent.numero_entidad
        cont.nombre_usuario = request.POST['nombre']
        cont.apellido_usuario = request.POST['apellido']
        cont.documento_usuario = request.POST['documento']
        
        cont.save()  
      
    return render(request,'RegistroClientes.html')
    
 