from django.urls import path
import apps.usuarios.views as views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.LoginUsuarioView.as_view(), name='login'),
    path('calculo-rapido/', views.calculo_rapido, name='calculo_rapido'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('calcular-notas/', views.calcular_notas, name='calcular_notas'),
    path('dashboard/', views.dashboard, name='dashboard'),
    #path('como-funciona/', views.como_funciona, name='como_funciona'),
    path('blog/', views.blog, name='blog'),
    path('contato/', views.contato, name='contato'),
]