from django.shortcuts import render
from perfis.models import Perfil

# Create your views here.
def index(request):
    return render(request, 'index.html', {'perfis': Perfil.objects.all()})

def exibir_perfil(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    return render(request, 'perfil.html', {'perfil': perfil})

def convidar(request, perfil_id):
    perfil_convidado = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_convidado)
    return redirect('index')

def get_perfil_logado(request):
    return Perfil.objects.get(id=1)