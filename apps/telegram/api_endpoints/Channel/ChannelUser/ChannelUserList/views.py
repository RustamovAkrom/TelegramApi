from rest_framework.generics import ListAPIView
from .serializers import ChannelUserListSerializer
from apps.telegram.models import ChannelUser


class ChannelUserListApiView(ListAPIView):
    queryset = ChannelUser.objects.all()
    serializer_class = ChannelUserListSerializer

__all__ = ("ChannelUserListApiView", )
