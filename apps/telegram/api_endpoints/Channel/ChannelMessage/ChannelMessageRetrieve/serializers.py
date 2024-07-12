from rest_framework.serializers import ModelSerializer
from apps.telegram.models import ChannelMessage


class ChannelMessageRetrieveSerializer(ModelSerializer):
    class Meta:
        model = ChannelMessage
        fields = ['user', 'message', 'media']
