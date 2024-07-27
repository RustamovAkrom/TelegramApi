from rest_framework.generics import CreateAPIView
from .serializers import ChannelMessageCreateSerializer
from apps.telegram.models import ChannelMessage


class ChannelMessageCreateApiView(CreateAPIView):
    queryset = ChannelMessage.objects.all()
    serializer_class = ChannelMessageCreateSerializer


__all__ = ("ChannelMessageCreateApiView",)
