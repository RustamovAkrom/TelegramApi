from rest_framework.generics import DestroyAPIView
from .serializers import ChannelStorieDestroySerializer
from apps.telegram.models import ChannelStories


class ChannelStorieDestroyApiView(DestroyAPIView):
    queryset = ChannelStories.objects.all()
    serializer_class = ChannelStorieDestroySerializer

__all__ = ("ChannelStorieDestroyApiView", )