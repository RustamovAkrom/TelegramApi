from rest_framework.generics import UpdateAPIView
from .serializers import ChannelUpdateSerializer
from apps.telegra.models import Channel


class ChannelUpdateApiView(UpdateAPIView):
    queryset = Channel
    serializer_class = ChannelUpdateSerializer

__all__ = ("ChannelUpdateApiView", )
