from rest_framework.generics import UpdateAPIView
from .serializers import ChatMessageUpdateSerializer
from apps.telegram.models import ChatMessage


class ChatMessageUpdateApiView(UpdateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageUpdateSerializer

__all__ = ("ChatMessageUpdateApiView", )
