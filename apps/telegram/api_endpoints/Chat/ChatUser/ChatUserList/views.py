from rest_framework.generics import ListAPIView
from .serializers import ChatUserListSerializer
from apps.telegram.models import ChatUser


class ChatUserListApiView(ListAPIView):
    queryset = ChatUser.objects.all()
    serializer_class = ChatUserListSerializer


__all__ = ("ChatUserListApiView",)
