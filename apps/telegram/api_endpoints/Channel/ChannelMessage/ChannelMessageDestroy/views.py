from rest_framework.generics import DestroyAPIView
from .serializers import ChannelMessageDestroySerializer
from apps.telegram.models import ChannelMessage


class ChannelMessageDestroyApiView(DestroyAPIView):
    queryset = ChannelMessage
    serializer_class = ChannelMessageDestroySerializer

__all__ = ("ChannelMessageDestroyApiView", )
