from rest_framework.generics import UpdateAPIView
from .serializers import ChannelMessageUpdateSerializer
from apps.telegram.models import ChannelMessage


class ChannelMessageUpdateApiView(UpdateAPIView):
    queryset = ChannelMessage.objects.all()
    serializer_class = ChannelMessageUpdateSerializer

__all__ = ("ChannelMessageUpdateApiView", )
