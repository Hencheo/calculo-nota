"""
WSGI config for calculo_notas project.
"""

import os
import sys

# Adicione o diretório raiz do projeto ao path do Python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

# Também adicione o diretório pai para garantir
parent_dir = os.path.dirname(BASE_DIR)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()