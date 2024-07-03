from rest_framework.serializers import ModelSerializer
from apps.account.models import Stories


class StorieListSerializer(ModelSerializer):
    class Meta:
        model = Stories
        fields = ("storie", "message")