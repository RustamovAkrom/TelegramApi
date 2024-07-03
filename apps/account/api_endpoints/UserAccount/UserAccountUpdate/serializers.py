from rest_framework.serializers import ModelSerializer
from apps.account.models import UserAccount


class UserAccountUpdateSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ("avatar", "bio", "first_name", "last_name", "username", "date_of_berth", "stories")
        