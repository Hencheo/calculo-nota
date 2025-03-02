from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.LoginUsuarioView.as_view(), name='login'),  # Corrigido para usar LoginUsuarioView
    path('logout/', views.logout_view, name='logout'),  # Substitua a view baseada em classe por função
    path('como-funciona/', views.como_funciona, name='como_funciona'),
    path('blog/', views.blog, name='blog'),
    path('contato/', views.contato, name='contato'),
    path('contato-simples/', views.contato_simples, name='contato_simples'),
    path('calcular/', views.calcular_notas, name='calcular_notas'),
    path('dashboard/', views.dashboard, name='dashboard'),
]