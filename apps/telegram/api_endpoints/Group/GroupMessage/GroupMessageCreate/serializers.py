from rest_framework.serializers import ModelSerializer
from apps.telegram.models import GroupMessage


class GroupMessageCreateSerializer(ModelSerializer):
    class Meta:
        model = GroupMessage
        fields = ['user', 'message', 'media']
