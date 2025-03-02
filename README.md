# Sistema de Cálculo de Notas

Um aplicativo web desenvolvido com Django para ajudar estudantes a calcular e gerenciar suas notas acadêmicas de forma simples e eficiente.

![Sistema de Cálculo de Notas](https://via.placeholder.com/800x400?text=Sistema+de+C%C3%A1lculo+de+Notas)

## 📋 Sobre o Projeto

O Sistema de Cálculo de Notas foi desenvolvido para simplificar a vida acadêmica dos estudantes, permitindo:

- Calcular médias ponderadas de acordo com os critérios da instituição
- Verificar automaticamente a situação acadêmica (aprovado, exame ou reprovado)
- Gerenciar disciplinas e notas em um dashboard personalizado
- Acompanhar o desempenho acadêmico ao longo do tempo

## ✨ Funcionalidades

- **Cálculo de Médias**: Cálculo automático baseado em pesos específicos (70% prova, 20% PIM, 10% AVA)
- **Verificação de Status**: Determina automaticamente se o aluno está aprovado, precisa de exame ou está reprovado
- **Dashboard Personalizado**: Visualização clara das disciplinas e desempenho
- **Sistema de Autenticação**: Registro e login de usuários para salvar histórico de notas
- **Design Responsivo**: Interface amigável que funciona em dispositivos móveis e desktop

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.0.1
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Banco de Dados**: SQLite (desenvolvimento)
- **Autenticação**: Django Authentication System
- **Estilização**: Font Awesome, CSS personalizado
- **Formulários**: Django Forms, Crispy Forms

## 📦 Instalação e Configuração

### Pré-requisitos
- Python 3.11+
- pip (gerenciador de pacotes Python)

### Passos para Instalação

1. Clone o repositório:
```bash
git clone https://github.com/hencheo/notas-faculdade.git
cd calculo-notas

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate
 ```

3. Instale as dependências:
```bash
pip install -r requirements.txt
 ```

4. Execute as migrações:
```bash
python manage.py migrate
 ```

5. Crie um superusuário (opcional):
```bash
python manage.py createsuperuser
 ```

6. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
 ```

7. Acesse o aplicativo em http://localhost:8000

## 🚀 Uso
1. Registre-se ou faça login no sistema
2. Acesse a calculadora de notas através do dashboard
3. Insira suas notas (prova, PIM e AVA)
4. Visualize instantaneamente sua média e situação acadêmica
5. Salve os resultados para consulta futura (requer login)

🔄 Fluxo de Trabalho
graph TD
    A[Usuário acessa o sistema] --> B{Possui conta?}
    B -->|Não| C[Registrar]
    B -->|Sim| D[Login]
    C --> E[Dashboard]
    D --> E
    E --> F[Calculadora de Notas]
    F --> G[Inserir Notas]
    G --> H[Calcular Média]
    H --> I{Média >= 7.0?}
    I -->|Sim| J[Aprovado]
    I -->|Não| K{Tem nota de exame?}
    K -->|Sim| L[Calcular Média Final]
    L --> M{Média Final >= 5.0?}
    M -->|Sim| N[Aprovado no Exame]
    M -->|Não| O[Reprovado]
    K -->|Não| P[Exame Necessário]


    ## 🤝 Contribuindo
Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature ( git checkout -b feature/nova-funcionalidade )
3. Faça commit das suas alterações ( git commit -m 'Adiciona nova funcionalidade' )
4. Faça push para a branch ( git push origin feature/nova-funcionalidade )
5. Abra um Pull Request
## 📄 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

## 📞 Contato
Hencheo - hencheo96@gmail.com

Link do Projeto: https://github.com/hencheo/notas-faculdade