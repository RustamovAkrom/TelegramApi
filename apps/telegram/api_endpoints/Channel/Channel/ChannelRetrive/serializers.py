from rest_framework.serializers import ModelSerializer
from apps.telegram.models import Channel


class ChannelRetriveSerializer(ModelSerializer):
    class Meta:
        model = Channel
        fields = ['photo', 'name', 'description', 'public_link', 'messages', 'users', 'stories']
