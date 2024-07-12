from rest_framework.serializers import ModelSerializer
from apps.telegram.models import ChannelUser


class ChannelUserDestroySerializer(ModelSerializer):
    class Meta:
        model = ChannelUser
        fields = ['user', 'is_owner', 'is_admin', 'is_active']
