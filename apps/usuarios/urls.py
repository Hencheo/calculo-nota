from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.LoginUsuarioView.as_view(), name='login'),
    # Usando LogoutView com next_page explícito para garantir redirecionamento para home
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('calcular-notas/', views.calcular_notas, name='calcular_notas'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('como-funciona/', views.como_funciona, name='como_funciona'),
    path('blog/', views.blog, name='blog'),
    path('contato/', views.contato, name='contato'),
]