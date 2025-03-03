from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    modalidade = forms.ChoiceField(
        choices=[('EAD', 'Ensino à Distância'), ('PRESENCIAL', 'Ensino Presencial')],
        label='Modalidade de Ensino',
        required=True,
        widget=forms.RadioSelect
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'modalidade']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Tornar os campos mais amigáveis
        self.fields['username'].help_text = 'Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.'
        self.fields['password1'].help_text = 'Sua senha deve conter pelo menos 8 caracteres e não pode ser muito comum.'
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Criar ou atualizar o perfil do usuário com a modalidade escolhida
            user.perfil.modalidade = self.cleaned_data['modalidade']
            user.perfil.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nome de usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Desativar o sistema de lembrar login e senha
        self.fields['username'].widget.attrs.update({'autocomplete': 'off'})
        self.fields['password'].widget.attrs.update({'autocomplete': 'off'})