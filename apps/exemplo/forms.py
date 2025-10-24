from .models import Exemplo
from django import forms


class ExemploForm(forms.ModelForm):
    """
    Classe de formulário para o modelo Exemplo.

    Este formulário é usado para criar e atualizar instâncias do modelo Exemplo.
    Ele define os campos, widgets, rótulos e textos de ajuda para cada campo.

    Atributos:
        model (Model): O modelo Exemplo associado ao formulário.
        fields (list): A lista de campos a serem exibidos no formulário.
        widgets (dict): Um dicionário que mapeia os campos aos widgets correspondentes.
        labels (dict): Um dicionário que mapeia os campos aos rótulos correspondentes.
        help_texts (dict): Um dicionário que mapeia os campos aos textos de ajuda correspondentes.
    """

    class Meta:
        model = Exemplo
        fields = ['nome', 'descricao']
        widgets = {
            # O que é form-control? Explicação Abaixo
            'nome': forms.TextInput(attrs={'class': 'form-control', 'id': 'nome'}),
            # O que é form-control? Explicação Abaixo
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'id': 'descricao'}),
        }
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição',
        }
        help_texts = {
            'nome': 'Nome do exemplo',
            'descricao': 'Descrição do exemplo',
        }

# O que é form-control?
# A classe "form-control" é uma classe CSS que é comumente usada em frameworks e bibliotecas de front-end, como o Bootstrap,
# para estilizar elementos de formulário, como campos de entrada de texto, áreas de texto, seletores e botões.
