from django.shortcuts import render, redirect
from perfis.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html',{'perfis': Perfil.objects.all(),'perfil_logado' : get_perfil_logado(request)})

def exibir_perfil(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    conectados = perfil in perfil_logado.contatos.all()
    return render(request, 'perfil.html', {'perfil': perfil,'perfil_logado' : get_perfil_logado(request), 'conectados' : conectados})

def convidar(request, perfil_id):
    perfil_convidado = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_convidado)
    return redirect('index')

def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')


def get_perfil_logado(request):
    return Perfil.objects.get(id=2)