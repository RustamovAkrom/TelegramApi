from rest_framework.generics import DestroyAPIView
from .serializers import ChannelStoriesDestroySerializer
from apps.telegram.models import ChannelStories


class ChannelStoriesDestroyApiView(DestroyAPIView):
    queryset = ChannelStories
    serializer_class = ChannelStoriesDestroySerializer

__all__ = ("ChannelStoriesDestroyApiView", )
