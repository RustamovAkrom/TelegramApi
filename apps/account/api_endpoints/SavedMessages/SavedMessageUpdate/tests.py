from django.urls import reverse
from apps.shared.tests import BaseSharedTestCase
from apps.account.models import User, UserAccount, SavedMessages


class SavedMessageListTest(BaseSharedTestCase):
    def setUp(self) -> None:
        self.user = self.create_user("Akromjon", "+998959896277", "2007")
        self.user.save()
        self.account = UserAccount.objects.get(user = self.user)
        return super().setUp()
    
    def test_list_saved_message(self):

        for i in range(1, 4):
            SavedMessages.objects.create(user = self.account, message = f"message{i}")

        for i in range(1, 4):
                
            url = self.url + reverse("account:saved-message-update", kwargs={"pk":i})
            data = {
                "user": self.account,
                "message": f"message{i * 2}"
            }
            response = self.client.put(path=url, data=data, headers=self.headers)
            response_data = response.json()
            print(response_data)
            print(response.status_code)