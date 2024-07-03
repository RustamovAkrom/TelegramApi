from rest_framework.serializers import ModelSerializer
from apps.account.models import UserAccount


class UserAccountCreateSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ("user", "avatar", "bio", "first_name", "last_name", "phone_number", "username", "date_of_berth", "stories")
        