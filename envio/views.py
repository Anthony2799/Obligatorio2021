from django.shortcuts import redirect, render
from django.http import HttpResponse
from envio.clases.group import Grupo
from envio.clases.grupos_cliente import grupos_cliente
from envio.clases.pago_normal import pago_normal
from envio.clases.pago_peso import pago_peso
from envio.clases.pago_distancia_peso import pago_distanica_peso
from django.template.response import TemplateResponse
from envio.forms import EnvioForm, PagoForm
from envio.pagos.Credito import Credito
from envio.pagos.Debito import Debito
from envio.pagos.Efectivo import Efectivo
from envio.pagos.Envio import Envio
from envio.pagos.Mercado_pago import Mercado_pago

from usuario.models import Entidad


def homeREturn(request):
    return render(request, 'home.html')


def alta_envio(request, **kwargs):
    print(request.POST)
    if request.method == 'POST':
        form = EnvioForm(request.POST)
        if form.is_valid():
            form.save()
        variable = Entidad.objects.all()
        valor = grupos_cliente()
        peso = float(request.POST.get('peso_paquete'))
        distancia = float(request.POST.get('distancia'))
        print(distancia)
        precio = 0
        for i in variable:

            if (request.POST.get('numero_entidad') == str(i.numero_entidad)):

                if str(i.numero_grupo) == 'P':

                    valor.setStrategy(pago_peso())
                    precio = valor.estrategia.execute(peso)
                    return redirect(f'http://localhost:8000/pagar/{str(precio)}')
                elif str(i.numero_grupo) == 'DP':

                    valor.setStrategy(pago_distanica_peso())
                    precio = valor.estrategia.execute(peso, distancia)
                    return redirect(f'http://localhost:8000/pagar/{str(precio)}')
                else:

                    valor.setStrategy()
                    precio = valor.estrategia.execute()
                    return redirect(f'http://localhost:8000/pagar/{str(precio)}')

    else:
        form = EnvioForm()
    return render(request, 'RegistroEnvio.html', {'form': form})


def homeREturn(request):
    return render(request, 'home.html')


def Pagar(request, precio):
    print(precio)

    form = PagoForm()
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            enviar = Envio()
            metod = request.POST.get('metodo')
            if str(metod) == 'Efectivo':
                enviar.setEstrategia(Efectivo())
                enviar.metodo_pago.devolucion(precio)
                print(PagoForm())
            if str(metod) == 'Debito':
                enviar.setEstrategia(Debito())
                enviar.metodo_pago.devolucion(precio, "afd")
                print(PagoForm())

            if str(metod) == 'Credito':
                enviar.setEstrategia(Credito())
                enviar.metodo_pago.devolucion(precio, "ada", "awdqw")
                print(PagoForm())

            if str(metod) == 'Mercado_pago':
                enviar.setEstrategia(Mercado_pago())
                enviar.metodo_pago.devolucion(precio, 'numero')
                print(PagoForm())

    else:
        if request.method == 'GET':
            form = PagoForm()
        context = {'nro_entidad': form
        }
        return render(request, 'pagar.html', context)


    return redirect('http://localhost:8000/')


