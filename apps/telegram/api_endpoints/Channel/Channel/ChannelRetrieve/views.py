from rest_framework.generics import RetrieveAPIView
from .serializers import ChannelRetrieveSerializer
from apps.telegram.models import Channel


class ChannelRetrieveApiView(RetrieveAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelRetrieveSerializer


__all__ = ("ChannelRetrieveApiView",)
