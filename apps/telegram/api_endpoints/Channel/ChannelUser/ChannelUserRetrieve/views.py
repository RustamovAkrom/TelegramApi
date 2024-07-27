from rest_framework.generics import RetrieveAPIView
from .serializers import ChannelUserRetrieveSerializer
from apps.telegram.models import ChannelUser


class ChannelUserRetrieveApiView(RetrieveAPIView):
    queryset = ChannelUser.objects.all()
    serializer_class = ChannelUserRetrieveSerializer


__all__ = ("ChannelUserRetrieveApiView",)
