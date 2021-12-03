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
        return redirect('RegistroClientes.html')
    else:
        form = ClienteForm()
    return render(request,'RegistroClientes.html',{'form':form})

def altaEntidad(request):
    if request.method == 'POST':
        form = EntidadForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('RegistroClientes.html')
    else:
        form = EntidadForm()
    return render(request,'RegistroClientes.html',{'form':form})

def altaEmpresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('RegistroClientes.html')
    else:
        form = EmpresaForm()
    return render(request,'RegistroClientes.html',{'form':form})