from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = "boilerplate.utils"

    def ready(self):
        from . import checks  # noqa
