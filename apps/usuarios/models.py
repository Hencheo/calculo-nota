from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Utilizamos o modelo de usuário padrão do Django
# Podemos estender com um perfil se necessário no futuro
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    data_nascimento = models.DateField('Data de Nascimento', null=True, blank=True)
    
    def __str__(self):
        return f'Perfil de {self.usuario.username}'
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        # Verifica se já existe um perfil para este usuário
        if not hasattr(instance, 'perfil'):
            Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def salvar_perfil_usuario(sender, instance, **kwargs):
    # Verifica se o usuário já tem um perfil antes de tentar salvar
    if hasattr(instance, 'perfil'):
        instance.perfil.save()