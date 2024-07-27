from django.test import TestCase
from config import settings
from apps.account.models import User, UserAccount


class BaseSharedTestCase(TestCase):
    jwt_token = settings.AUTHENTICATION_TOKEN

    headers = {"Authorization": f"bearer {jwt_token}"}
    data = {}
    url = "http://127.0.0.1:8000"

    def create_user(self, username, phone_number, password) -> User:
        user = User.objects.create(username=username, phone_number=phone_number)
        user.set_password(password)
        user.save()
        user.token = self.jwt_token
        user.is_active = True
        self.user = user
        UserAccount.objects.create(
            user=user, username=user.username, phone_number=user.phone_number
        )
        return self.user
