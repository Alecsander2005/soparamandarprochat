from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Usuario, TimeUsuario, CardCriminoso

@receiver(post_save, sender=User)
def create_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance, nome=instance.username, email=instance.email)

@receiver(m2m_changed, sender=TimeUsuario.cards.through)
def validate_cards(sender, instance, action, pk_set, **kwargs):
    if action == "pre_add":
        cards_atuais = set(instance.cards.all().values_list('pk', flat=True))
        cards_novos = cards_atuais.union(pk_set)
        
        if len(cards_novos) > 10:
            print(f'Você não pode ter mais de 10 cards no time.')
            pk_set.clear()
            return
        
        recompensas = {}
        cards = CardCriminoso.objects.filter(pk__in=cards_novos)
        for card in cards:
            recompensas[card.recompensa] = recompensas.get(card.recompensa, 0) + 1
            if recompensas[card.recompensa] > 2:
                print(f'Você não pode ter mais de 2 cards com a recompensa {card.recompensa}.')
                pk_set.clear()
                return