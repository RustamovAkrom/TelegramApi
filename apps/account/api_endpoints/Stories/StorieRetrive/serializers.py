from rest_framework.serializers import ModelSerializer
from apps.account.models import Stories


class StorieRetriveSerializer(ModelSerializer):
    class Meta:
        model = Stories
        fields = ("storie", "message")
        