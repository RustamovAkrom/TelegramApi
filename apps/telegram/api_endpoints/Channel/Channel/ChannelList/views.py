from rest_framework.generics import ListAPIView
from .serializers import ChannelListSerializer
from apps.telegram.models import Channel


class ChannelListApiView(ListAPIView):
    queryset = Channel
    serializer_class = ChannelListSerializer

__all__ = ("ChannelListApiView", )
