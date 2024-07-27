from rest_framework.generics import CreateAPIView
from .serializers import ChannelUserCreateSerializer
from apps.telegram.models import ChannelUser


class ChannelUserCreateApiView(CreateAPIView):
    queryset = ChannelUser.objects.all()
    serializer_class = ChannelUserCreateSerializer


__all__ = ("ChannelUserCreateApiView",)
