from django import forms
from .models import Disciplina

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'nota_prova1', 'nota_prova2', 'nota_pim', 'nota_ava', 'nota_exame']
        widgets = {
            'nota_prova1': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '10'}),
            'nota_prova2': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '10'}),
            'nota_pim': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '10'}),
            'nota_ava': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '10'}),
            'nota_exame': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '10'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ajusta os campos visíveis com base na modalidade do usuário
        if 'instance' in kwargs and kwargs['instance'] is None and 'initial' in kwargs:
            # Novo formulário
            if 'usuario' in kwargs['initial']:
                usuario = kwargs['initial']['usuario']
                modalidade = usuario.perfil.modalidade
                if modalidade == 'EAD':
                    self.fields['nota_prova2'].widget = forms.HiddenInput()
                    self.fields['nota_prova2'].required = False
                else:  # PRESENCIAL
                    self.fields['nota_ava'].widget = forms.HiddenInput()
                    self.fields['nota_ava'].required = False
        elif 'instance' in kwargs and kwargs['instance'] is not None:
            # Edição de formulário existente
            modalidade = kwargs['instance'].usuario.perfil.modalidade
            if modalidade == 'EAD':
                self.fields['nota_prova2'].widget = forms.HiddenInput()
                self.fields['nota_prova2'].required = False
            else:  # PRESENCIAL
                self.fields['nota_ava'].widget = forms.HiddenInput()
                self.fields['nota_ava'].required = False