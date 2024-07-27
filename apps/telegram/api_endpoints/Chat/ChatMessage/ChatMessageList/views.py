from rest_framework.generics import ListAPIView
from .serializers import ChatMessageListSerializer
from apps.telegram.models import ChatMessage


class ChatMessageListApiView(ListAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageListSerializer


__all__ = ("ChatMessageListApiView",)
