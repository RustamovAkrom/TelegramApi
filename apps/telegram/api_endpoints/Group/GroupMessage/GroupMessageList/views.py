from rest_framework.generics import ListAPIView
from .serializers import GroupMessageListSerializer
from apps.telegram.models import GroupMessage


class GroupMessageListApiView(ListAPIView):
    queryset = GroupMessage.objects.all()
    serializer_class = GroupMessageListSerializer

__all__ = ("GroupMessageListApiView", )
