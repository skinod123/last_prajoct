from django.apps import AppConfig


class RockayConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "rockay"

class AccountsConfig(AppConfig):
    name = 'accounts'

   
 # def ready(self):