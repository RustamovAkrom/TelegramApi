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
        saved_message = SavedMessages.objects.create(
            user=self.account, message="message1"
        )

        url = self.url + reverse(
            "account:saved-message-update", kwargs={"pk": saved_message.pk}
        )

        data = {"user": self.account, "message": "message updated"}

        response = self.client.patch(
            path=url, data=data, format="json", accept="application/data"
        )
        print(response.status_code)
        print(response.json())
