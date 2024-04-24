from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    def ready(self):
        import users.signals

from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = "users"

    def ready(self):
        # Makes sure all signal handlers are connected
        from users import handlers  # noqa