from rest_framework.serializers import ModelSerializer
from apps.telegram.models import GroupMessage


class GroupMessageRetrieveSerializer(ModelSerializer):
    class Meta:
        model = GroupMessage
        fields = ['user', 'message', 'media']
