from rest_framework.generics import CreateAPIView
from .serializers import ChannelStoriesCreateSerializer
from apps.telegram.models import ChannelStories


class ChannelStoriesCreateApiView(CreateAPIView):
    queryset = ChannelStories
    serializer_class = ChannelStoriesCreateSerializer

__all__ = ("ChannelStoriesCreateApiView", )
