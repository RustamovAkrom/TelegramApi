from django.urls import reverse
from apps.shared.tests import BaseSharedTestCase
from apps.account.models import User, UserAccount, SavedMessages


class SavedMessageListTest(BaseSharedTestCase):
    def setUp(self) -> None:
        self.user = self.create_user("Akromjon", "+998959896277", "2007")
        self.user.save()
        self.account = UserAccount.objects.get(user=self.user)
        return super().setUp()

    def test_list_saved_message(self):
        url = self.url + reverse("account:saved-message-list")

        for i in range(3):
            SavedMessages.objects.create(user=self.account, message=f"message{i}")

        response = self.client.get(path=url, data=self.data, headers=self.headers)
        response_data = response.json()
        self.assertEqual(response.status_code, 200)

        for data in response_data:
            saved_message = SavedMessages.objects.filter(
                user=self.account, message=data["message"]
            )
            self.assertTrue(saved_message.exists())
