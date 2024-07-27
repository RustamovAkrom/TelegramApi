from rest_framework.generics import CreateAPIView
from .serializers import ChatCreateSerializer
from apps.telegram.models import Chat


class ChatCreateApiView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatCreateSerializer


__all__ = ("ChatCreateApiView",)
