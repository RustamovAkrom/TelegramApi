from rest_framework.generics import ListAPIView
from .serializers import ChannelDiscussionListSerializer
from apps.telegram.models import ChannelDiscusion


class ChannelDiscussionListApiView(ListAPIView):
    queryset = ChannelDiscusion.objects.all()
    serializer_class = ChannelDiscussionListSerializer

__all__ = ("ChannelDiscussionListApiView", )