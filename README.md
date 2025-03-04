# Sistema de Cálculo de Notas

Um aplicativo web desenvolvido com Django para ajudar estudantes a calcular e gerenciar suas notas acadêmicas de forma simples e eficiente.

![Sistema de Cálculo de Notas](https://via.placeholder.com/800x400?text=Sistema+de+C%C3%A1lculo+de+Notas)

## 📋 Sobre o Projeto

O Sistema de Cálculo de Notas foi desenvolvido para simplificar a vida acadêmica dos estudantes, permitindo:

- Calcular médias ponderadas de acordo com os critérios da instituição
- Verificar automaticamente a situação acadêmica (aprovado, exame ou reprovado)
- Gerenciar disciplinas e notas em um dashboard personalizado
- Acompanhar o desempenho acadêmico ao longo do tempo
- Suporte para diferentes modalidades de ensino (Presencial e EAD)

## ✨ Funcionalidades

- **Cálculo de Médias**: Cálculo automático baseado em pesos específicos (70% prova, 20% PIM, 10% AVA)
- **Verificação de Status**: Determina automaticamente se o aluno está aprovado, precisa de exame ou está reprovado
- **Dashboard Personalizado**: Visualização clara das disciplinas e desempenho
- **Sistema de Autenticação**: Registro e login de usuários para salvar histórico de notas
- **Design Responsivo**: Interface amigável que funciona em dispositivos móveis e desktop
- **Cálculo Rápido**: Opção para calcular notas sem necessidade de cadastro
- **Suporte a Múltiplas Modalidades**: Cálculos específicos para ensino presencial e à distância
- **Blog Integrado**: Artigos e dicas sobre vida acadêmica

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.0.1
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Banco de Dados**: SQLite (desenvolvimento)
- **Autenticação**: Sistema de Autenticação do Django
- **Estilização**: Font Awesome, CSS personalizado, Swiper
- **Formulários**: Django Forms, Crispy Forms
- **Efeitos Visuais**: Animações CSS, Backdrop Filter

## 📦 Instalação e Configuração

### Pré-requisitos
- Python 3.11+
- pip (gerenciador de pacotes Python)

### Passos para Instalação

1. Clone o repositório:
```bash
git clone https://github.com/hencheo/notas-faculdade.git
cd calculo_notas
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione sua chave secreta: `SECRET_KEY=sua-chave-secreta-aqui`

5. Execute as migrações:
```bash
python manage.py migrate
```

6. Crie um superusuário (opcional):
```bash
python manage.py createsuperuser
```

7. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

8. Acesse o aplicativo em http://localhost:8000

## 🚀 Como Usar

### Uso Sem Cadastro
1. Acesse a página inicial
2. Clique em "Cálculo Rápido"
3. Selecione a modalidade (Presencial ou EAD)
4. Insira suas notas (prova, PIM e AVA)
5. Visualize instantaneamente sua média e situação acadêmica

### Uso Com Cadastro
1. Registre-se ou faça login no sistema
2. Acesse o dashboard personalizado
3. Adicione suas disciplinas
4. Insira as notas para cada disciplina
5. Acompanhe seu desempenho acadêmico
6. Salve os resultados para consulta futura

## 📱 Recursos da Interface

- **Design Responsivo**: Adaptado para todos os tamanhos de tela
- **Tema Moderno**: Interface com efeitos de vidro (glassmorphism) e gradientes
- **Navegação Intuitiva**: Menu simplificado com ícones
- **Feedback Visual**: Alertas e mensagens informativas
- **Modo Mobile**: Otimizado para dispositivos com telas pequenas

## 🔄 Fluxo de Trabalho

```
Usuário acessa o sistema
    ↓
Possui conta?
    ↓       ↓
   Não     Sim
    ↓       ↓
Registrar  Login
    ↓       ↓
    ↓→ Dashboard ←↓
        ↓
Calculadora de Notas
        ↓
Inserir Notas
        ↓
Calcular Média
        ↓
Média >= 7.0?
    ↓       ↓
   Sim     Não
    ↓       ↓
Aprovado   Tem nota de exame?
            ↓       ↓
           Sim     Não
            ↓       ↓
    Calcular Média Final   Exame Necessário
            ↓
    Média Final >= 5.0?
            ↓       ↓
           Sim     Não
            ↓       ↓
    Aprovado no Exame   Reprovado
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Faça push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 🐛 Reportando Problemas

Encontrou um bug ou tem uma sugestão? Abra uma issue descrevendo o problema ou a melhoria sugerida.

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

## 📞 Contato

Hencheo - hencheo96@gmail.com

Link do Projeto: https://github.com/hencheo/notas-faculdade