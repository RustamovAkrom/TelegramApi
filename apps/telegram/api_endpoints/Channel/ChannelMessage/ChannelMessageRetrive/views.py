from rest_framework.generics import RetriveAPIView
from .serializers import ChannelMessageRetriveSerializer
from apps.telegram.models import ChannelMessage


class ChannelMessageRetriveApiView(RetriveAPIView):
    queryset = ChannelMessage
    serializer_class = ChannelMessageRetriveSerializer

__all__ = ("ChannelMessageRetriveApiView", )
