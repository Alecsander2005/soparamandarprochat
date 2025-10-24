from django import forms
from .models import CardCriminoso, TimeUsuario, Usuario

class CardCriminosoForm(forms.ModelForm):
    criado_em = forms.DateTimeField(disabled=True, required=False)
    atualizado_em = forms.DateTimeField(disabled=True, required=False)
    recompensa = forms.ChoiceField(choices=CardCriminoso.recompensa_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    faccao = forms.ChoiceField(choices=CardCriminoso.FACCAO, widget=forms.Select(attrs={'class': 'form-control'}))
    validade = forms.ChoiceField(choices=CardCriminoso.validade_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    crime = forms.ChoiceField(choices=CardCriminoso.CRIMES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = CardCriminoso
        fields = [
            'nome', 'apelido', 'tempo', 'recompensa', 'faccao',
            'validade', 'crime', 'imagem'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'apelido': forms.TextInput(attrs={'class': 'form-control'}),
            'tempo': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome',
            'apelido': 'Apelido',
            'tempo': 'Tempo de Foragido',
            'recompensa': 'Recompensa',
            'faccao': 'Facção',
            'crime': 'Crime Cometido',
            'imagem': 'Foto do Criminoso',
            'criado_em': 'Criado em',
            'atualizado_em': 'Atualizado em',
            'validade': 'Validade do Card',
        }
        help_texts = {
            'nome': 'Nome completo do criminoso.',
            'apelido': 'Apelido conhecido nas ruas.',
            'tempo': 'Quantidade de anos de cadeia.',
            'recompensa': 'Valor da recompensa.',
            'faccao': 'Facção criminosa do indivíduo.',
            'crime': 'Descreva o crime mais cabuloso do meliante.',
            'imagem': 'Envie uma imagem do indivíduo.',
            'criado_em': 'Data de criação do card (somente leitura).',
            'atualizado_em': 'Data da última atualização do card (somente leitura).',
            'validade': 'Tempo de validade do card em dias.',
        }


class TimeUsuarioForm(forms.ModelForm):
    class Meta:
        model = TimeUsuario
        fields = ['cards']
        widgets = {
            'cards': forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}),
        }
        labels = {
            'cards': 'Escolha os criminosos pro seu time',
        }
        help_texts = {
            'cards': 'Selecione os cards que vão compor o time do usuário.',
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'time']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'id': 'nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}),
            'time': forms.Select(attrs={'class': 'form-control', 'id': 'time'}),
        }
        labels = {
            'nome': 'Nome do Usuário',
            'email': 'E-mail',
            'time': 'Time de Criminosos',
        }
        help_texts = {
            'nome': 'Nome completo do usuário.',
            'email': 'Informe um e-mail válido.',
            'time': 'Selecione um time já existente (pode deixar em branco).',
        }
