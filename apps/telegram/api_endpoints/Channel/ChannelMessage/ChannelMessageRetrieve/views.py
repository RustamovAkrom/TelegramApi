from rest_framework.generics import RetrieveAPIView
from .serializers import ChannelMessageRetrieveSerializer
from apps.telegram.models import ChannelMessage


class ChannelMessageRetrieveApiView(RetrieveAPIView):
    queryset = ChannelMessage.objects.all()
    serializer_class = ChannelMessageRetrieveSerializer

__all__ = ("ChannelMessageRetrieveApiView", )
