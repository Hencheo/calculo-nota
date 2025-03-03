from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class Disciplina(models.Model):
    nome = models.CharField('Nome da Disciplina', max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota_prova1 = models.DecimalField('Nota da Prova 1', max_digits=4, decimal_places=2, null=True, blank=True)
    nota_prova2 = models.DecimalField('Nota da Prova 2', max_digits=4, decimal_places=2, null=True, blank=True)
    nota_pim = models.DecimalField('Nota do PIM', max_digits=4, decimal_places=2, null=True, blank=True)
    nota_ava = models.DecimalField('Nota dos Questionários AVA', max_digits=4, decimal_places=2, null=True, blank=True)
    nota_exame = models.DecimalField('Nota do Exame', max_digits=4, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def calcular_media(self):
        modalidade = self.usuario.perfil.modalidade
        
        if modalidade == 'EAD':
            if all(nota is not None for nota in [self.nota_prova1, self.nota_pim, self.nota_ava]):
                return (Decimal('7.0') * self.nota_prova1 + 
                       Decimal('2.0') * self.nota_pim + 
                       Decimal('1.0') * self.nota_ava) / Decimal('10.0')
        else:  # PRESENCIAL
            if all(nota is not None for nota in [self.nota_prova1, self.nota_prova2, self.nota_pim]):
                return ((self.nota_prova1 + self.nota_prova2) * Decimal('0.8') + 
                       self.nota_pim * Decimal('0.2')) / Decimal('2.0')
        return None

    def calcular_media_final(self):
        media = self.calcular_media()
        if media is None:
            return None, 'Pendente'
        
        if media >= Decimal('7.0'):
            return media, 'Aprovado'
        
        if self.nota_exame is not None:
            media_final = (media + self.nota_exame) / Decimal('2.0')
            if media_final >= Decimal('5.0'):
                return media_final, 'Aprovado após exame'
            return media_final, 'Reprovado'
        
        return media, 'Exame necessário'

    def __str__(self):
        return f"{self.nome} - {self.usuario.username}"

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ['-created_at']