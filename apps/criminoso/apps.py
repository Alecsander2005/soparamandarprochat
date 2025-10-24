from django.apps import AppConfig


class CriminosoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.criminoso'
    
    def ready(self):
        import apps.criminoso.signals
