from rest_framework.generics import CreateAPIView
from .serializers import ChannelCreateSerializer
from apps.telegram.models import Channel


class ChannelCreateApiView(CreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelCreateSerializer


__all__ = ("ChannelCreateApiView",)
