from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'


class MyAppConfig(AppConfig):
    name = "posts"

    def ready(self):
        # Makes sure all signal handlers are connected
        from posts import handlers  # noqa