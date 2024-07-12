from rest_framework.serializers import ModelSerializer
from apps.telegra.models import Channel


class ChannelRetriveSerializer:
    class Meta:
        model = Channel
        fields = ['photo', ' name description', ' public_link', ' messages', ' users', ' stories', ' discusions']
