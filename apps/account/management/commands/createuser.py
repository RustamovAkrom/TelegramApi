from django.core.management.base import BaseCommand
from apps.account.models import User, UserAccount


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.create_superuser("Akrmjon2", "akromjonrustamov56@gmail.com", "2007", "+998958786298")

    def create_superuser(self, username, email, password, phone_number):
        if not User.objects.filter(username = username).exists():
            account = UserAccount.objects.create(username = username)

            user = User.objects.create(
                account = account,
                is_staff = True,
                is_superuser = True,
                username = username
            )
            user.set_password(password)
            user.save()

            self.stdout.write(self.style.SUCCESS("Superuser successfully created"))
        else:
            self.stdout.write(
                self.style.ERROR("Superuser already exists.")
            )