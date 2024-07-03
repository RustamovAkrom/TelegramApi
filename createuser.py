import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()

from apps.account.models import User, UserAccount


user = User(
    is_active = True,
    is_staff = True,
    is_superuser = True,
    username = input("Username: "),
    phone_number = input("Phone Number:"),
)
user.set_password(input("Password"))
user.save()
UserAccount.objects.create(user = user, username = user.username, phone_number = user.phone_number)
