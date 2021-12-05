from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from envio.clases.group import Grupo
from envio.clases.grupos_cliente import grupos_cliente
from envio.clases.pago_normal import pago_normal
from envio.clases.pago_peso import pago_peso
from envio.clases.pago_distancia_peso import pago_distanica_peso

from envio.forms import EnvioForm, PagoForm

from usuario.models import Entidad


def homeREturn(request):
    return render(request, 'home.html')

def alta_envio(request):
    if request.method == 'POST':
        form = EnvioForm(request.POST)
        if form.is_valid():
            form.save()
        variable = Entidad.objects.all()
        valor = grupos_cliente()
        peso = float(request.POST.get('peso_paquete'))
        distancia = float(request.POST.get('distancia'))
        for i in variable:
            if(request.POST.get('numero_entidad') == str(i.numero_entidad)):
                if str(i.numero_grupo) == 'P':
                    valor.setStrategy(pago_peso())
                    valor.estrategia.execute(peso)
                    print(valor.estrategia.execute(peso))
                elif str(i.numero_grupo) == 'DP':
                    valor.setStrategy(pago_distanica_peso())
                    valor.estrategia.execute(peso,distancia)
                    print(valor.estrategia.execute(peso,distancia))
                else:
                    valor.setStrategy()
                    valor.estrategia.execute()
                    print(valor.estrategia.execute())
    else:
        form = EnvioForm()
    return render(request,'RegistroEnvio.html',{'form':form})

def homeREturn(request):
    return render(request, 'home.html')

def Pagar(request):
    print(request.POST)
    form = PagoForm()
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
          print(PagoForm())
    else:
        form = PagoForm()
    context={
        'nro_entidad': form    
    }
    return render(request,'pagar.html',context)
    
 