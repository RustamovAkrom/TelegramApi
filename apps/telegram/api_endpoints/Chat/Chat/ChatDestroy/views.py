from rest_framework.generics import DestroyAPIView
from .serializers import ChatDestroySerializer
from apps.telegram.models import Chat


class ChatDestroyApiView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatDestroySerializer


__all__ = ("ChatDestroyApiView",)
