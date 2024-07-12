from rest_framework.generics import UpdateAPIView
from .serializers import ChannelStoriesUpdateSerializer
from apps.telegram.models import ChannelStories


class ChannelStoriesUpdateApiView(UpdateAPIView):
    queryset = ChannelStories
    serializer_class = ChannelStoriesUpdateSerializer

__all__ = ("ChannelStoriesUpdateApiView", )
