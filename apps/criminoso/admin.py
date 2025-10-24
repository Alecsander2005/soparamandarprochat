from django.contrib import admin
from .models import CardCriminoso, TimeUsuario, Usuario 

# Register your models here.
@admin.register(CardCriminoso)
class CardCriminosoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'apelido', 'tempo', 'recompensa', 'crime') 
    list_display_links = ('id', 'nome', 'apelido')  
    search_fields = ('nome', 'apelido', 'crime')  
    list_per_page = 10  
    ordering = ('-recompensa',) 

@admin.register(TimeUsuario)
class TimeUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'listar_cards')
    search_fields = ('cards__nome', 'cards__apelido')
    list_per_page = 10

    def listar_cards(self, obj):
        return ", ".join([card.nome for card in obj.cards.all()])
    listar_cards.short_description = 'Cards do Time'

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'nome', 'email', 'time')
    search_fields = ('user__username', 'nome', 'email')
    list_per_page = 10
    list_filter = ('time',)