from rest_framework.generics import CreateAPIView
from .serializers import ChannelStorieCreateSerializer
from apps.telegram.models import ChannelStories


class ChannelStorieCreateApiView(CreateAPIView):
    queryset = ChannelStories.objects.all()
    serializer_class = ChannelStorieCreateSerializer

__all__ = ("ChannelStorieCreateApiView", )