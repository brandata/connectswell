from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "connectswell.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
