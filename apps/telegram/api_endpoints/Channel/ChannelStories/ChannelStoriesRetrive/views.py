from rest_framework.generics import RetriveAPIView
from .serializers import ChannelStoriesRetriveSerializer
from apps.telegram.models import ChannelStories


class ChannelStoriesRetriveApiView(RetriveAPIView):
    queryset = ChannelStories
    serializer_class = ChannelStoriesRetriveSerializer

__all__ = ("ChannelStoriesRetriveApiView", )
