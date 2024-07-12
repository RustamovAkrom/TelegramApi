from rest_framework.generics import ListAPIView
from .serializers import ChannelListSerializer
from apps.telegra.models import Channel


class ChannelListApiView(ListAPIView):
    queryset = Channel
    serializer_class = ChannelListSerializer

__all__ = ("ChannelListApiView", )
