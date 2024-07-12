from rest_framework.generics import UpdateAPIView
from .serializers import ChatUpdateSerializer
from apps.telegram.models import Chat


class ChatUpdateApiView(UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatUpdateSerializer

__all__ = ("ChatUpdateApiView", )
