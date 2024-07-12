from rest_framework.generics import RetrieveAPIView
from .serializers import ChannelStorieUpdateSerializer
from apps.telegram.models import ChannelStories


class ChannelStorieRetriveApiView(RetrieveAPIView):
    queryset = ChannelStories.objects.all()
    serializer_class = ChannelStorieUpdateSerializer

__all__ = ("ChannelStorieRetriveApiView", )