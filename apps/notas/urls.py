from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('disciplina/adicionar/', views.adicionar_disciplina, name='adicionar_disciplina'),
    path('disciplina/<int:pk>/editar/', views.editar_disciplina, name='editar_disciplina'),
    path('disciplina/<int:pk>/excluir/', views.excluir_disciplina, name='excluir_disciplina'),
]