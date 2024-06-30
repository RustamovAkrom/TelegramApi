from rest_framework.generics import UpdateAPIView
from apps.account.models import SavedMessages
from .serializers import SavedMessageUpdateSerializer


class SavedMessageUpdateApiView(UpdateAPIView):
    queryset = SavedMessages.objects.all()
    serializer_class = SavedMessageUpdateSerializer

__all__ = ("SavedMessageUpdateApiView", )