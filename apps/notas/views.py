from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Disciplina
from .forms import DisciplinaForm

@login_required
def dashboard(request):
    disciplinas = Disciplina.objects.filter(usuario=request.user)
    return render(request, 'notas/dashboard.html', {'disciplinas': disciplinas})

@login_required
def disciplina_criar(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            disciplina = form.save(commit=False)
            disciplina.usuario = request.user
            disciplina.save()
            messages.success(request, 'Disciplina criada com sucesso!')
            return redirect('dashboard')
    else:
        form = DisciplinaForm()
    return render(request, 'notas/disciplina_form.html', {'form': form, 'titulo': 'Nova Disciplina'})

@login_required
def disciplina_editar(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            messages.success(request, 'Disciplina atualizada com sucesso!')
            return redirect('dashboard')
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'notas/disciplina_form.html', {'form': form, 'titulo': 'Editar Disciplina'})

@login_required
def disciplina_excluir(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk, usuario=request.user)
    if request.method == 'POST':
        disciplina.delete()
        messages.success(request, 'Disciplina excluída com sucesso!')
        return redirect('dashboard')
    return render(request, 'notas/disciplina_confirmar_exclusao.html', {'disciplina': disciplina})