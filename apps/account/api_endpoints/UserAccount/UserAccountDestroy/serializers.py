from rest_framework.serializers import ModelSerializer
from apps.account.models import UserAccount


class UserAccountDestroySerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ("user")