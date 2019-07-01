from django.shortcuts import render, redirect

from .models import Equipe

from .form import EquipeForm

# Create your views here.
def index(request):
    return render(request, 'app_teste/index.html')

def listar(request):

    dado = {}
    dado['equipes'] = Equipe.objects.all()
    #dado['equipe'] = Equipe.objects.filter()

    return render(request, 'app_teste/listar.html', dado)


def cadastro(request):
    #form = EquipeForm()

    #verificar se tem algo preenchido
    form = EquipeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar')

    return render(request, 'app_teste/criar.html', {'form': form})


def atualizar(request, pk):
    equipe = Equipe.objects.get(pk=pk)

    form = EquipeForm(request.POST or None, instance=equipe)

    if form.is_valid():
        form.save()
        return redirect('listar')

    return render(request, 'app_teste/criar.html', {'form': form})

def deletar(request, pk):
    equipe = Equipe.objects.get(pk=pk)
    equipe.delete()
    return redirect('listar')
    

