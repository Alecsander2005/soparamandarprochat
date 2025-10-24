from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import User
from django.db import IntegrityError

from apps.portal.models import Gender, OrganizationalHierarchy, Entity, Enjoyer, Military


class Command(BaseCommand):
    help = 'Deletes all records from specified models safely, handling deletions individually.'

    def handle(self, *args, **options):
        # Proteção contra exclusões em produção
        if not settings.DEBUG:
            self.stdout.write(self.style.ERROR('This command can only be run in DEBUG mode.'))
            return
        # Confirmação para prosseguir
        self.stdout.write(self.style.WARNING('This will attempt to delete all data individually from User, Gender, OrganizationalHierarchy, Entity, Enjoyer, and Military models.'))
        if input("Type 'yes' to continue: ") != 'yes':
            self.stdout.write(self.style.ERROR('Operation cancelled.'))
            return

        # Lista de modelos para limpeza, incluindo o modelo User do Django
        models = [User, Enjoyer, Military, Entity, Gender, OrganizationalHierarchy]
        total_deleted = 0

        for model in models:
            model_name = model.__name__
            for instance in model.objects.all():
                try:
                    instance.delete()
                    self.stdout.write(self.style.SUCCESS(f'Successfully deleted: {instance} from {model_name}.'))
                    total_deleted += 1
                except IntegrityError as e:
                    self.stdout.write(self.style.ERROR(f'Could not delete {instance} from {model_name}: {str(e)}'))

        self.stdout.write(self.style.SUCCESS(f'Total records deleted: {total_deleted}'))
        self.stdout.write(self.style.SUCCESS('Data deletion attempt completed.'))
