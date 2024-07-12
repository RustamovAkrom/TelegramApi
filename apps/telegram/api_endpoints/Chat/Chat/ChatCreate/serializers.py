from rest_framework.serializers import ModelSerializer
from apps.telegram.models import Chat


class ChatCreateSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = ['user_from', 'user_to']