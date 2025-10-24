from .models import ExemploImagens
from django.contrib import admin

# Register your models here.

# Registrar modelo no site django admin.


@admin.register(ExemploImagens)
class ExemploImagensAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'imagem', 'editado', 'criado')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10
    ordering = ('-criado',)
