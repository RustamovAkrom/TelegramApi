from rest_framework.generics import RetrieveAPIView
from .serializers import ChatMessageRetrieveSerializer
from apps.telegram.models import ChatMessage


class ChatMessageRetrieveApiView(RetrieveAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageRetrieveSerializer


__all__ = ("ChatMessageRetrieveApiView",)
