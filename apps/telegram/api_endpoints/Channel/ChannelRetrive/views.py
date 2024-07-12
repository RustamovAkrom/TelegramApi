from rest_framework.generics import RetriveAPIView
from .serializers import ChannelRetriveSerializer
from apps.telegra.models import Channel


class ChannelRetriveApiView(RetriveAPIView):
    queryset = Channel
    serializer_class = ChannelRetriveSerializer

__all__ = ("ChannelRetriveApiView", )
