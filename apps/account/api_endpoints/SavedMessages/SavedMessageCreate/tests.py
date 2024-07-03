from django.urls import reverse
from apps.shared.tests import BaseSharedTestCase
from apps.account.models import User, UserAccount


class TestSavedMessageCreateTest(BaseSharedTestCase):
    
    def test_create_saved_message(self):
        self.create_user("Akromjon", "_998959896277", "2007")

        url = self.url + reverse("account:saved-message-create")
        self.data['user'] = self.user.pk,
        self.data['message'] = "message1"

        response = self.client.post(path = url,data=self.data, headers = self.headers)
        response_data = response.json()
    
        self.assertEqual((response_data['user'], ), self.data['user'])
        self.assertEqual(response_data['message'], self.data['message'])
        self.assertEqual(response.status_code, 201)