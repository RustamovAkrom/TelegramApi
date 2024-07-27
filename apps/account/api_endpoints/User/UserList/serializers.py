from rest_framework.serializers import ModelSerializer
from apps.account.models import User


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("phone_number", "username", "password", "is_active")
