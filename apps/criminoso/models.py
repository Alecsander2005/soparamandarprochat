from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import timedelta, datetime, date

class CardCriminoso(models.Model):
    CRIMES = [
        ('ASSALTO', 'Assalto'),
        ('ESTUPRO', 'Estupro'),
        ('FURTO', 'Furto'),
        ('MAO_ARMADA', 'Mão Armada'),
    ]
    FACCAO = [
        ('OKAIDA', 'Okaida'),
        ('COMANDO VERMELHO', 'Comando Vermelho (CV)'),
        ('PCC', 'Primeiro Comando da Capital (PCC)'),
        ('ADA', 'Amigos dos Amigos'),
        ('TCP', 'Terceiro Comando'),
        ('CN', 'Comando Nordeste'),
        ('EUA', 'Estados Unidos'),

    ]

    recompensa_choices = [
        ('$', '$'),
        ('$$', '$$'),
        ('$$$', '$$$'),
        ('$$$$', '$$$$'),
        ('$$$$$', '$$$$$')
    ]
    
    validade_choices = [
        (15, '15 dias'),
        (30, '30 dias'),
        (60, '60 dias'),
        (90, '90 dias'),
    ]

    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)
    tempo = models.IntegerField()
    recompensa = models.CharField(max_length=5, choices=recompensa_choices, default='$')
    crime = models.CharField(max_length=20, choices=CRIMES)
    faccao = models.CharField(max_length=40, choices=FACCAO)  # max_length ajustado!
    imagem = models.ImageField(upload_to='imagens_criminosos/')
    ativo = models.BooleanField(default=True)
    validade = models.IntegerField(choices=validade_choices, default=30)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.nome} - {self.apelido}'
    
    def is_valid(self):
        hoje = date.today()
        data_expiracao = self.criado_em.date() + timedelta(days=self.validade)
        if hoje > data_expiracao:
            if self.ativo:
                self.ativo = False
                self.save(update_fields=['ativo'])
            return False
        else:
            if not self.ativo:
                self.ativo = True
                self.save(update_fields=['ativo'])
            return True

class TimeUsuario(models.Model):
    cards = models.ManyToManyField(CardCriminoso, related_name='times')

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    time = models.OneToOneField('TimeUsuario', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
