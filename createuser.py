import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()

from apps.account.models import User, UserAccount

account = UserAccount.objects.create(phone_number = "+20203040s", username = "Akromjon4")

user = User.objects.create(
    account = account,
    is_staff = True,
    is_superuser = True,
    username = "Akromjon4",
    phone_number = "+20203040s",
)

user.set_password("2007")
user.save()

# account.phone_number = user.phone_number
# account.username = user.username
# account.save()