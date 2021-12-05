from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from envio.clases.group import Grupo
from envio.clases.pago import pago
from envio.clases.pago_normal import pago_normal
from envio.clases.pago_peso import pago_peso
from envio.clases.pago_distancia_peso import pago_distanica_peso
from envio.forms import EnvioForm
from usuario.models import Entidad


def homeREturn(request):
    return render(request, 'home.html')

def alta_envio(request):
    if request.method == 'POST':
        form = EnvioForm(request.POST)
        if form.is_valid():
            form.save()
        variable = Entidad.objects.all()
        for i in variable:
             print(i)
             if(request.POST.get('numero_entidad') == str(i.numero_entidad)):
                 valor = pago()
                 if i.numero_grupo == 'P':
                     valor.setStrategy(pago_peso())
                     peso = float(request.POST.get('peso_paquete'))
                     print(peso)
                     valor.executeStrategy(peso)
                 elif i.numero_grupo == 'DP':
                     valor.setStrategy(pago_distanica_peso())
                     valor.executeStrategy(float(request.POST.get('peso')),12)
                 else:
                     valor.setStrategy(pago_normal())
                     valor.executeStrategy()
    else:
        form = EnvioForm()
        return render(request,'RegistroEnvio.html',{'form':form})

def homeREturn(request):
    return render(request, 'home.html')
 