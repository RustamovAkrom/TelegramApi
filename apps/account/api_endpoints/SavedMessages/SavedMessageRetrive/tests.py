from django.urls import reverse
from apps.shared.tests import BaseSharedTestCase
from apps.account.models import User, UserAccount, SavedMessages


class SavedMessageRetrive(BaseSharedTestCase):
    def setUp(self) -> None:
        self.user = self.create_user("Akromjon", "+998959896277", "2007")
        self.user.save()
        self.account = UserAccount.objects.get(user = self.user)
        return super().setUp()
    
    def test_retrive_saved_message(self):

        for i in range(1, 4):
            SavedMessages.objects.create(user = self.account, message = f"message{i}")

        for i in range(1, 4):
            url = self.url + reverse("account:saved-message-retrive", kwargs={"pk": i})
            response = self.client.get(path=url, data=self.data, headers=self.headers)
            response_data = response.json()
            saved_message = SavedMessages.objects.filter(user = response_data["user"], message = response_data['message'])
            self.assertTrue(saved_message.exists())
            self.assertEqual(response.status_code, 200)