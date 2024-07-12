from rest_framework.serializers import ModelSerializer
from apps.telegram.models import ChatUser


class ChatUserListSerializer(ModelSerializer):
    class Meta:
        model = ChatUser
        fields = ['user', 'is_active']
