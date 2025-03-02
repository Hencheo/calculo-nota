from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('disciplina/nova/', views.disciplina_criar, name='disciplina_criar'),
    path('disciplina/<int:pk>/editar/', views.disciplina_editar, name='disciplina_editar'),
    path('disciplina/<int:pk>/excluir/', views.disciplina_excluir, name='disciplina_excluir'),
]