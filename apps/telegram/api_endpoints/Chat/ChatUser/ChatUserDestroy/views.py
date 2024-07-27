from rest_framework.generics import DestroyAPIView
from .serializers import ChatUserDestroySerializer
from apps.telegram.models import ChatUser


class ChatUserDestroyApiView(DestroyAPIView):
    queryset = ChatUser.objects.all()
    serializer_class = ChatUserDestroySerializer


__all__ = ("ChatUserDestroyApiView",)
