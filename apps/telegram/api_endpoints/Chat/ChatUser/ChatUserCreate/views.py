from rest_framework.generics import CreateAPIView
from .serializers import ChatUserCreateSerializer
from apps.telegram.models import ChatUser


class ChatUserCreateApiView(CreateAPIView):
    queryset = ChatUser.objects.all()
    serializer_class = ChatUserCreateSerializer

__all__ = ("ChatUserCreateApiView", )
