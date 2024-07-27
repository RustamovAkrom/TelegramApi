from rest_framework.generics import CreateAPIView
from .serializers import ChatMessageCreateSerializer
from apps.telegram.models import ChatMessage


class ChatMessageCreateApiView(CreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageCreateSerializer


__all__ = ("ChatMessageCreateApiView",)
