from rest_framework.serializers import ModelSerializer
from apps.telegram.models import Group


class GroupCreateSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ["photo", "name", "description", "public_link", "messages", "users"]
