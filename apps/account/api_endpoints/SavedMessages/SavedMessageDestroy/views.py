from rest_framework.generics import DestroyAPIView
from apps.account.models import SavedMessages
from .serializers import SavedMessageDestroySerializer

class SavedMessageDestroyApiView(DestroyAPIView):
    queryset = SavedMessages.objects.all()
    serializer_class = SavedMessageDestroySerializer


__all__ = ("SavedMessageDestroyApiView", )