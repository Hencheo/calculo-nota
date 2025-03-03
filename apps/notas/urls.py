from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('disciplinas/', views.listar_disciplinas, name='listar_disciplinas'),
    path('disciplinas/adicionar/', views.adicionar_disciplina, name='adicionar_disciplina'),
    path('disciplinas/<int:pk>/editar/', views.editar_disciplina, name='editar_disciplina'),
    path('disciplinas/<int:pk>/excluir/', views.excluir_disciplina, name='excluir_disciplina'),
]