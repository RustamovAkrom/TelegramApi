from rest_framework.generics import RetrieveAPIView
from .serializers import ChannelDiscusionRetriveSerializer
from apps.telegram.models import ChannelDiscusion


class ChannelDiscussionRetriveApiView(RetrieveAPIView):
    queryset = ChannelDiscusion.objects.all()
    serializer_class = ChannelDiscusionRetriveSerializer

__all__ = ("ChannelDiscussionRetriveApiView", )