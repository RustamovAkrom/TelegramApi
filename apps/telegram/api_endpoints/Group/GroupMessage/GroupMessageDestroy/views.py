from rest_framework.generics import DestroyAPIView
from .serializers import GroupMessageDestroySerializer
from apps.telegram.models import GroupMessage


class GroupMessageDestroyApiView(DestroyAPIView):
    queryset = GroupMessage.objects.all()
    serializer_class = GroupMessageDestroySerializer


__all__ = ("GroupMessageDestroyApiView",)
