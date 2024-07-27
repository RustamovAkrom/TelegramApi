from rest_framework.generics import ListAPIView
from .serializers import ChatListSerializer
from apps.telegram.models import Chat


class ChatListApiView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatListSerializer


__all__ = ("ChatListApiView",)
