from rest_framework.generics import UpdateAPIView
from .serializers import GroupMessageUpdateSerializer
from apps.telegram.models import GroupMessage


class GroupMessageUpdateApiView(UpdateAPIView):
    queryset = GroupMessage.objects.all()
    serializer_class = GroupMessageUpdateSerializer


__all__ = ("GroupMessageUpdateApiView",)
