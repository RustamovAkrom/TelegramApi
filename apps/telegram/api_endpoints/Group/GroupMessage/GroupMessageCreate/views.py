from rest_framework.generics import CreateAPIView
from .serializers import GroupMessageCreateSerializer
from apps.telegram.models import GroupMessage


class GroupMessageCreateApiView(CreateAPIView):
    queryset = GroupMessage.objects.all()
    serializer_class = GroupMessageCreateSerializer

__all__ = ("GroupMessageCreateApiView", )
