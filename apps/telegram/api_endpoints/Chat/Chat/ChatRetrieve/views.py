from rest_framework.generics import RetrieveAPIView
from .serializers import ChatRetrieveSerializer
from apps.telegram.models import Chat


class ChatRetrieveApiView(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatRetrieveSerializer

__all__ = ("ChatRetrieveApiView", )
