from rest_framework.generics import DestroyAPIView
from .serializers import ChannelUserDestroySerializer
from apps.telegram.models import ChannelUser


class ChannelUserDestroyApiView(DestroyAPIView):
    queryset = ChannelUser
    serializer_class = ChannelUserDestroySerializer

__all__ = ("ChannelUserDestroyApiView", )
