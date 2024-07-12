from rest_framework.serializers import ModelSerializer
from apps.telegram.models import ChannelStories


class ChannelStorieDestroySerializer(ModelSerializer):
    class Meta:
        model = ChannelStories
        fields = ['storie', 'message']