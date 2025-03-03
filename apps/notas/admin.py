from django.contrib import admin
from .models import Disciplina

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'usuario', 'nota_prova1', 'nota_pim', 'nota_ava', 'nota_exame', 'get_media', 'get_situacao')
    list_filter = ('usuario',)
    search_fields = ('nome', 'usuario__username')
    
    def get_media(self, obj):
        media, _ = obj.calcular_media_final()
        return media if media is not None else '-'
    get_media.short_description = 'Média'
    
    def get_situacao(self, obj):
        _, situacao = obj.calcular_media_final()
        return situacao
    get_situacao.short_description = 'Situação'