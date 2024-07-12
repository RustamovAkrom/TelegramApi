from rest_framework.serializers import ModelSerializer
from apps.telegram.models import ChatMessage


class ChatMessageRetrieveSerializer(ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['user', 'message', 'media']
