from rest_framework.generics import ListAPIView
from .serializers import ChannelStoriesListSerializer
from apps.telegram.models import ChannelStories


class ChannelStoriesListApiView(ListAPIView):
    queryset = ChannelStories
    serializer_class = ChannelStoriesListSerializer

__all__ = ("ChannelStoriesListApiView", )
