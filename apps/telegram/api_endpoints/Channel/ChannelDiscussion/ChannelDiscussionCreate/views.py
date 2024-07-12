from rest_framework.generics import CreateAPIView
from .serializers import ChannelDiscussionCreateSerializer
from apps.telegram.models import ChannelDiscusion


class ChanneDiscussionCreateApiView(CreateAPIView):
    queryset = ChannelDiscusion.objects.all()
    serializer_class = ChannelDiscussionCreateSerializer

__all__ = ("ChanneDiscussionCreateApiView", )