from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from usuario.forms import ClienteForm,EntidadForm,EmpresaForm

def infex(request):
    return render(request,'index.html')


def altaCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid:
            form.save()

    else:
        form = ClienteForm()
    return render(request,'RegistroClientes.html',{'form':form})


# Alta de entidad
def alta_entidad(request):
    if request.method == 'POST':
        form = EntidadForm(request.POST)
        print(form)
        if form.is_valid:
            form.save()
            
    else:
        form = EntidadForm()
    if form['empresa'].value() == True:
        return render(request,'agregar_empresa.html',{'form':form})
    else:
        return render(request,'agregar_entidad.html',{'form':form})


# Agregar empresa
def altaEmpresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid:
            form.save()

    else:
        form = EmpresaForm()
    return render(request,'RegistroClientes.html',{'form':form})