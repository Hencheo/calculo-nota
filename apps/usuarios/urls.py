from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # Remova as outras definições de logout e mantenha apenas esta
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('calcular-notas/', views.calcular_notas, name='calcular_notas'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('como-funciona/', views.como_funciona, name='como_funciona'),
    path('blog/', views.blog, name='blog'),
    path('contato/', views.contato, name='contato'),
    # Certifique-se de que esta URL está usando a função correta
    path('logout/', views.logout_view, name='logout'),
    # OU use a classe do Django com next_page definido
    # path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    # Use a view de logout do Django diretamente
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]