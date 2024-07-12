from rest_framework.generics import RetrieveAPIView
from .serializers import ChatUserRetrieveSerializer
from apps.telegram.models import ChatUser


class ChatUserRetrieveApiView(RetrieveAPIView):
    queryset = ChatUser.objects.all()
    serializer_class = ChatUserRetrieveSerializer

__all__ = ("ChatUserRetrieveApiView", )
