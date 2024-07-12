from rest_framework.generics import RetrieveAPIView
from .serializers import ChannelRetriveSerializer
from apps.telegram.models import Channel


class ChannelRetriveApiView(RetrieveAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelRetriveSerializer

__all__ = ("ChannelRetriveApiView", )
