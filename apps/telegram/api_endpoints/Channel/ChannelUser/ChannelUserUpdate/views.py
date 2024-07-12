from rest_framework.generics import UpdateAPIView
from .serializers import ChannelUserUpdateSerializer
from apps.telegram.models import ChannelUser


class ChannelUserUpdateApiView(UpdateAPIView):
    queryset = ChannelUser
    serializer_class = ChannelUserUpdateSerializer

__all__ = ("ChannelUserUpdateApiView", )