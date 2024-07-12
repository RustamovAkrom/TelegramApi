from rest_framework.serializers import ModelSerializer
from apps.telegram.models import ChannelDiscusion


class ChannelDiscussionListSerializer(ModelSerializer):
    class Meta:
        model = ChannelDiscusion
        fields = ("user", "message", "media", "discusions")