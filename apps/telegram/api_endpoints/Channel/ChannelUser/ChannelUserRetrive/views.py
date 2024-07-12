from rest_framework.generics import RetriveAPIView
from .serializers import ChannelUserRetriveSerializer
from apps.telegram.models import ChannelUser


class ChannelUserRetriveApiView(RetriveAPIView):
    queryset = ChannelUser
    serializer_class = ChannelUserRetriveSerializer

__all__ = ("ChannelUserRetriveApiView", )
