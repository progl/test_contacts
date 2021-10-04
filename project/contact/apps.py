from django.apps import AppConfig


class ContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'

    # noinspection PyUnresolvedReferences
    def ready(self):
        from . import signals
