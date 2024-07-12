from rest_framework.generics import ListAPIView
from .serializers import ChannelMessageListSerializer
from apps.telegram.models import ChannelMessage


class ChannelMessageListApiView(ListAPIView):
    queryset = ChannelMessage
    serializer_class = ChannelMessageListSerializer

__all__ = ("ChannelMessageListApiView", )