from rest_framework.generics import DestroyAPIView
from .serializers import ChatMessageDestroySerializer
from apps.telegram.models import ChatMessage


class ChatMessageDestroyApiView(DestroyAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageDestroySerializer

__all__ = ("ChatMessageDestroyApiView", )
