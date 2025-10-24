# apps/criminoso/urls.py

from django.urls import path, include
from . import views

app_name = 'criminoso'

urlpatterns = [
    # Card Criminoso
    path('card_criminoso/', views.CardCriminosoView.as_view(), name='card_criminoso'),
    path('card_criminoso/cadastrar/', views.CardCriminosoCreateView.as_view(), name='card_cadastro'),
    path('card_criminoso/atualizar/<int:pk>', views.CardCriminosoUpdateView.as_view(), name='card_atualizar'),
    path('card_criminoso/deletar/<int:pk>', views.CardCriminosoDeleteView.as_view(), name='card_deletar'),
    path('card_criminoso/listar/', views.CardCriminosoListView.as_view(), name='card_listar'),
    path('card_criminoso/listar/<int:pk>', views.CardCriminosoDetailView.as_view(), name='card_detalhe'),
    
    # URL para Escalar Criminoso (agora usando a nova Class-Based View)
    path('card_criminoso/<int:pk>/escalar/', views.EscalarCriminosoView.as_view(), name='escalar_criminoso'),

    # Time Usuario
    path('time_usuario/', views.TimeUsuarioView.as_view(), name='time_usuario'), # Esta view agora passa os cards escalados
    path('time_usuario/cadastrar/', views.TimeUsuarioCreateView.as_view(), name='time_cadastro'),
    path('time_usuario/atualizar/<int:pk>', views.TimeUsuarioUpdateView.as_view(), name='time_atualizar'),
    path('time_usuario/deletar/<int:pk>', views.TimeUsuarioDeleteView.as_view(), name='time_deletar'),
    path('time_usuario/listar/', views.TimeUsuarioListView.as_view(), name='time_listar'),
    path('time_usuario/listar/<int:pk>', views.TimeUsuarioDetailView.as_view(), name='time_detalhe'),
]