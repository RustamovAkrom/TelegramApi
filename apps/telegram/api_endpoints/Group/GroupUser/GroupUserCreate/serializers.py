from rest_framework.serializers import ModelSerializer
from apps.telegram.models import GroupUser


class GroupUserCreateSerializer(ModelSerializer):
    class Meta:
        model = GroupUser
        fields = ['user', 'is_owner', 'is_admin', 'is_active']
