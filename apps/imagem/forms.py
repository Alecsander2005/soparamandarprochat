from .models import ExemploImagens
from django import forms


class ExemploImagemForm(forms.ModelForm):
    class Meta:
        model = ExemploImagens
        fields = ['nome', 'imagem']
        widgets = {
            # O que é form-control? Explicação no app exemplo.
            'nome': forms.TextInput(attrs={'class': 'form-control', 'id': 'nome'}),
            # O que é custom-file-input? Explicação Abaixo.
            'imagem': forms.FileInput(attrs={'class': 'custom-file-input', 'id': 'imagem'}),
        }
        labels = {
            'nome': 'Nome',
            'imagem': 'Imagem',
        }
        help_texts = {
            'nome': 'Nome do exemplo',
            'imagem': 'Imagem do exemplo',
        }

# O que é custom-file-input?
# A classe "custom-file-input" é uma classe CSS que é comumente usada em frameworks e bibliotecas de front-end, como o Bootstrap,
# para estilizar elementos de formulário, como campos de entrada de texto, áreas de texto, seletores e botões.
