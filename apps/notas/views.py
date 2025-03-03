from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Disciplina
from .forms import DisciplinaForm

@login_required
def listar_disciplinas(request):
    disciplinas = Disciplina.objects.filter(usuario=request.user)
    return render(request, 'notas/listar_disciplinas.html', {'disciplinas': disciplinas})

@login_required
def adicionar_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            disciplina = form.save(commit=False)
            disciplina.usuario = request.user
            disciplina.save()
            messages.success(request, 'Disciplina adicionada com sucesso!')
            return redirect('listar_disciplinas')
    else:
        form = DisciplinaForm()
    return render(request, 'notas/form_disciplina.html', {'form': form, 'titulo': 'Adicionar Disciplina'})

@login_required
def editar_disciplina(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            messages.success(request, 'Disciplina atualizada com sucesso!')
            return redirect('listar_disciplinas')
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'notas/form_disciplina.html', {'form': form, 'titulo': 'Editar Disciplina'})

@login_required
def excluir_disciplina(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk, usuario=request.user)
    if request.method == 'POST':
        disciplina.delete()
        messages.success(request, 'Disciplina excluída com sucesso!')
        return redirect('listar_disciplinas')
    return render(request, 'notas/confirmar_exclusao.html', {'disciplina': disciplina})

@login_required
def dashboard(request):
    disciplinas = Disciplina.objects.filter(usuario=request.user)
    context = {
        'disciplinas': disciplinas,
        'total_disciplinas': disciplinas.count(),
        'aprovadas': sum(1 for d in disciplinas if d.calcular_media_final()[1] == 'Aprovado'),
        'em_exame': sum(1 for d in disciplinas if d.calcular_media_final()[1] == 'Exame necessário'),
        'reprovadas': sum(1 for d in disciplinas if d.calcular_media_final()[1] == 'Reprovado'),
    }
    return render(request, 'notas/dashboard.html', context)