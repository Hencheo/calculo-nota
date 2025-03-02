from django import forms
from .models import Disciplina

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'nota_prova', 'nota_pim', 'nota_ava', 'nota_exame']
        widgets = {
            'nota_prova': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '10'}),
            'nota_pim': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '10'}),
            'nota_ava': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '10'}),
            'nota_exame': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '10'}),
        }