from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.account"

    def ready(self) -> None:
        import apps.account.signals
        return super().ready()