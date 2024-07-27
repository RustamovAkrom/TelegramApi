from rest_framework.generics import CreateAPIView
from apps.account.models import SavedMessages
from .serializers import SavedMessagesSerializer


class SavedMessageCreateApiView(CreateAPIView):
    queryset = SavedMessages.objects.all()
    serializer_class = SavedMessagesSerializer


__all__ = ("SavedMessageCreateApiView",)
