from rest_framework.generics import UpdateAPIView
from .serializers import ChatUserUpdateSerializer
from apps.telegram.models import ChatUser


class ChatUserUpdateApiView(UpdateAPIView):
    queryset = ChatUser.objects.all()
    serializer_class = ChatUserUpdateSerializer

__all__ = ("ChatUserUpdateApiView", )
