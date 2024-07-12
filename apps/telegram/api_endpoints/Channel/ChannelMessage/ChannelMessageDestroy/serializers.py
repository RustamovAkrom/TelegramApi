from rest_framework.serializers import ModelSerializer
from apps.telegram.models import ChannelMessage


class ChannelMessageDestroySerializer:
    class Meta:
        model = ChannelMessage
        fields = ('user', 'message', 'media', 'discusions')
