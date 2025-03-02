#!/bin/bash
# exit on error
set -o errexit

# Atualizar pip e instalar dependências
python -m pip install --upgrade pip
pip install -r requirements.txt

# Coletar arquivos estáticos e executar migrações
python manage.py collectstatic --no-input
python manage.py migrate