from rest_framework.generics import UpdateAPIView
from .serializers import ChannelDiscusionUpdateSerializer
from apps.telegram.models import ChannelDiscusion


class ChannelDiscussionUpdateApiView(UpdateAPIView):
    queryset = ChannelDiscusion.objects.all()
    serializer_class = ChannelDiscusionUpdateSerializer

__all__ = ("ChannelDiscussionUpdateApiView", )