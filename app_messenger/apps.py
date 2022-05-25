from django.apps import AppConfig


class AppMessengerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_messenger'

    def ready(self):
        import app_messenger.signals