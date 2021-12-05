from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from usuario.forms import ClienteForm,EntidadForm,EmpresaForm





def altaCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = ClienteForm()
    return render(request,'RegistroClientes.html',{'form':form})


# Alta de entidad
def altaentidad(request):
    
    if request.method == 'POST':
        form = EntidadForm(request.POST)
        es_empresa = form['empresa'].value()
        
        if form.is_valid():
            
            form.save()
            if es_empresa:
                return redirect('http://localhost:8000/agregar_empresa/')
            else:
                return redirect('http://localhost:8000/AltaCliente/')

    else:
        form = EmpresaForm()
        return render(request,'agregar_entidad.html',{'form': form })
   

# Agregar empresa
def altaEmpresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmpresaForm()
    return render(request,'RegistroClientes.html',{'form':form})

