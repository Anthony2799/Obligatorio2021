from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from envio.forms import EnvioForm


def homeREturn(request):
    return render(request, 'home.html')

def alta_envio(request):
    if request.method == 'POST':
        form = EnvioForm(request.POST)
        if form.is_valid():
            form.save()
            attach(form.save)
    else:
        form = EnvioForm()
    return render(request,'RegistroEnvio.html',{'form':form})

observers = []

def attach(self, observer):
    if not observer in self._observers:
        self._observers.append(observer)

def detach(self, observer):
    try:
        self._observers.remove(observer)
    except ValueError:
         pass

def notify(self,**kargs):
    for observer in self._observers:
        observer.update(self,**kargs)