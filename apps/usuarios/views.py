from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout  # Adicione logout aqui
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse
from .forms import RegistroUsuarioForm, LoginForm

from django.contrib.auth.decorators import login_required

# Adicione esta função às suas views existentes
def calcular_notas(request):
    """
    Renderiza a página de cálculo de notas
    """
    return render(request, 'usuarios/calculo.html')

@login_required
def dashboard(request):
    """
    Renderiza a página de dashboard do usuário
    Requer que o usuário esteja autenticado
    """
    return render(request, 'usuarios/dashboard.html', {
        'page_title': 'Dashboard',
        'user': request.user
    })

# Adicione esta função para registro baseado em função
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Fazer login automático após o cadastro
            login(request, user)
            messages.success(request, f'Conta criada com sucesso! Bem-vindo, {user.username}!')
            # Redireciona para o dashboard após o cadastro
            return redirect('dashboard')  
        else:
            # Se o formulário não for válido, exibir mensagens de erro
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Erro no campo {field}: {error}')
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})

# Ajuste a classe LoginUsuarioView para garantir redirecionamento para o dashboard
class LoginUsuarioView(LoginView):
    form_class = LoginForm
    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True  # Redireciona usuários já autenticados
    
    def get_success_url(self):
        return reverse_lazy('dashboard')
    
    def form_valid(self, form):
        messages.success(self.request, f'Bem-vindo de volta, {form.get_user().username}!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Nome de usuário ou senha inválidos.')
        return super().form_invalid(form)
    def form_valid(self, form):
        messages.success(self.request, f'Bem-vindo, {form.get_user().first_name}!')
        return super().form_valid(form)

class LogoutUsuarioView(LogoutView):
    next_page = reverse_lazy('login')
    
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Você saiu do sistema com sucesso!')
        return super().dispatch(request, *args, **kwargs)

# Substitua a classe LogoutUsuarioView por uma função baseada em view
def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu do sistema com sucesso!')
    return redirect('home')  # Redireciona para a página inicial após logout

def home(request):
    return render(request, 'usuarios/home.html')

def como_funciona(request):
    return render(request, 'usuarios/como_funciona.html')

def blog(request):
    return render(request, 'usuarios/blog.html')

def contato(request):
    return render(request, 'usuarios/contato.html')

def contato_simples(request):
    html = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contato - Sistema de Cálculo de Notas</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <div class="container">
                <a class="navbar-brand" href="/">
                    <i class="fas fa-calculator me-2"></i>Cálculo de Notas
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav me-auto">
                        <li class="nav-item">
                            <a class="nav-link" href="/como-funciona/">Como Funciona</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/blog/">Blog</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" href="/contato/">Contato</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <div class="container py-5">
            <div class="row justify-content-center">
                <div class="col-md-8">
                    <div class="card">
                        <div class="card-header bg-primary text-white">
                            <h3 class="mb-0"><i class="fas fa-envelope me-2"></i>Entre em Contato</h3>
                        </div>
                        <div class="card-body">
                            <div class="alert alert-info mb-4">
                                <i class="fas fa-info-circle me-2"></i>
                                Para dúvidas ou sugestões, envie um email para: 
                                <a href="mailto:hencheo96@gmail.com">hencheo96@gmail.com</a>
                            </div>
                            <form>
                                <div class="mb-3">
                                    <label for="nome" class="form-label">Nome</label>
                                    <input type="text" class="form-control" id="nome" placeholder="Seu nome completo">
                                </div>
                                <div class="mb-3">
                                    <label for="email" class="form-label">E-mail</label>
                                    <input type="email" class="form-control" id="email" placeholder="seu.email@exemplo.com">
                                </div>
                                <div class="mb-3">
                                    <label for="assunto" class="form-label">Assunto</label>
                                    <input type="text" class="form-control" id="assunto" placeholder="Assunto da mensagem">
                                </div>
                                <div class="mb-3">
                                    <label for="mensagem" class="form-label">Mensagem</label>
                                    <textarea class="form-control" id="mensagem" rows="5" placeholder="Digite sua mensagem aqui..."></textarea>
                                </div>
                                <button type="submit" class="btn btn-primary">
                                    <i class="fas fa-paper-plane me-2"></i>Enviar Mensagem
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    return HttpResponse(html)