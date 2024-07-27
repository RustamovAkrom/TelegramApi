from rest_framework.serializers import ModelSerializer
from apps.telegram.models import Chat


class ChatRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = ["user_from", "user_to"]
