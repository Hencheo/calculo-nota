from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('calcular-notas/', views.calcular_notas, name='calcular_notas'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('como-funciona/', views.como_funciona, name='como_funciona'),
    path('blog/', views.blog, name='blog'),
    path('contato/', views.contato, name='contato'),
]