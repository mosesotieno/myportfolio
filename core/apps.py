from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_initial_data(sender, **kwargs):
    from core.models import Profile
    # Your data creation logic here

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        post_migrate.connect(create_initial_data, sender=self)