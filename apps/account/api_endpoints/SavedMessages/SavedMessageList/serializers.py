from rest_framework.serializers import ModelSerializer
from apps.account.models import SavedMessages


class SavedMessageListSerializer(ModelSerializer):
    class Meta:
        model = SavedMessages
        fields = ("user", "message")