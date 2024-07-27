from rest_framework.serializers import ModelSerializer
from rest_framework import fields
from apps.account.models import UserAccount, User, Stories


class MiniUserRetriveSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("token", "is_active", "phone_number", "username")


class MiniStorieRetriveSerializer(ModelSerializer):
    class Meta:
        model = Stories
        fields = ("storie", "message")


class UserAccountRetriveSerializer(ModelSerializer):
    user = MiniUserRetriveSerializer(read_only=True)
    stories = MiniStorieRetriveSerializer(many=True, read_only=True)

    class Meta:
        model = UserAccount
        fields = (
            "user",
            "avatar",
            "bio",
            "first_name",
            "last_name",
            "phone_number",
            "username",
            "date_of_berth",
            "stories",
        )
