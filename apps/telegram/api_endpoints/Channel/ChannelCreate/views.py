from rest_framework.generics import CreateAPIView
from .serializers import ChannelCreateSerializer
from apps.telegra.models import Channel


class ChannelCreateApiView(CreateAPIView):
    queryset = Channel
    serializer_class = ChannelCreateSerializer

__all__ = ("ChannelCreateApiView", )
