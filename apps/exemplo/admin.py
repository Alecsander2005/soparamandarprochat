from django.contrib import admin
from .models import Exemplo
# Register your models here.

# Registrar modelo no site django admin.


@admin.register(Exemplo)
class ExemploAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'editado', 'criado')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10
    ordering = ('-criado',)
