# apps/portal/tasks.py
from django.contrib.auth.models import User
from celery import shared_task
import logging

from . import models

logger = logging.getLogger(__name__)


@shared_task(bind=True)
def link_military(self, username):
    """
    Relaciona o militar a um usuário através de seu username
    """
    print("#"*30)
    militaries = models.Military.objects.filter(cpf=username, user__isnull=True)
    print("#"*30)
    for military in militaries:
        user = User.objects.get(username=username)
        military.user = user
        military.save()
        logger.info('Military linked successful with User Django behind username: {}'.format(username))
        
        
@shared_task(bind=True)
def link_enjoyer(self, username):
    """
    Relaciona o utilizador a um usuário através de seu username
    """
    
    enjoyers = models.Enjoyer.objects.filter(username=username, user__isnull=True)
    
    for enjoyer in enjoyers:
        user = User.objects.get(username=username)
        enjoyer.user = user
        enjoyer.save()
        logger.info('Enjoyer linked successful with User Django behind username: {}'.format(username))


