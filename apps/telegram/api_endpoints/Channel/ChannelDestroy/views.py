from rest_framework.generics import DestroyAPIView
from .serializers import ChannelDestroySerializer
from apps.telegra.models import Channel


class ChannelDestroyApiView(DestroyAPIView):
    queryset = Channel
    serializer_class = ChannelDestroySerializer

__all__ = ("ChannelDestroyApiView", )
