from rest_framework.serializers import ModelSerializer
from apps.account.models import User


class UserDestroySerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = ("")
