from rest_framework.generics import ListAPIView
from .serializers import ChannelStorieListSerializer
from apps.telegram.models import ChannelStories


class ChannelStorieListApiView(ListAPIView):
    queryset = ChannelStories.objects.all()
    serializer_class = ChannelStorieListSerializer

__all__ = ("ChannelStorieListApiView", )