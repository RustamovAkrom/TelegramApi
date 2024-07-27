from rest_framework.serializers import ModelSerializer
from apps.telegram.models import ChannelStories


class ChannelStorieListSerializer(ModelSerializer):
    class Meta:
        model = ChannelStories
        fields = ["storie", "message"]
