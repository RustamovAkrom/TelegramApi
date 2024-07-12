from rest_framework.generics import DestroyAPIView
from .serializers import ChannelDiscussionDestroySerializer
from apps.telegram.models import ChannelDiscusion


class ChannelDiscussionDestroyApiView(DestroyAPIView):
    queryset = ChannelDiscusion.objects.all()
    serializer_class = ChannelDiscussionDestroySerializer

__all__ = ("ChannelDiscussionDestroyApiView", )