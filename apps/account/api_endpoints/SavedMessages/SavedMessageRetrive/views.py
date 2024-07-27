from rest_framework.generics import RetrieveAPIView
from apps.account.models import SavedMessages
from .serializers import SavedMessageRetriveSerializer


class SavedMessageRetriveApiView(RetrieveAPIView):
    queryset = SavedMessages.objects.all()
    serializer_class = SavedMessageRetriveSerializer


__all__ = ("SavedMessageRetriveApiView",)
