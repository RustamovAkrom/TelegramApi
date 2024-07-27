from django.urls import reverse
from apps.shared.tests import BaseSharedTestCase
from apps.account.models import User, UserAccount, SavedMessages


class SavedMessageDestroyTest(BaseSharedTestCase):

    def setUp(self):
        self.user = self.create_user("Akromjon", "+998959896277", "2007")
        self.user.save()
        self.account = UserAccount.objects.get(user=self.user)

        return super().setUp()

    def test_create_saved_message(self):

        url = self.url + reverse("account:saved-message-create")
        self.data["user"] = (self.account.pk,)
        self.data["message"] = "message1"

        response = self.client.post(path=url, data=self.data, headers=self.headers)
        response_data = response.json()

        self.assertEqual((response_data["user"],), self.data["user"])
        self.assertEqual(response_data["message"], self.data["message"])
        self.assertEqual(response.status_code, 201)

    def test_destroy_saved_message(self):
        SavedMessages.objects.create(user=self.account, message="message2")
        url = self.url + reverse(
            "account:saved-message-destroy", kwargs={"pk": self.user.pk}
        )

        response = self.client.delete(path=url, data=self.data, headers=self.headers)
        self.assertEqual(response.status_code, 204)
