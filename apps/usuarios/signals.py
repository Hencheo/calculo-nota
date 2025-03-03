from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Perfil

@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    """Cria um perfil para cada novo usuário criado"""
    if created:
        # Verifica se já existe um perfil para este usuário
        if not hasattr(instance, 'perfil'):
            Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def salvar_perfil_usuario(sender, instance, **kwargs):
    """Garante que o perfil seja salvo quando o usuário for atualizado"""
    # Verifica se o usuário já tem um perfil antes de tentar salvar
    if hasattr(instance, 'perfil'):
        instance.perfil.save()