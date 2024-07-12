from rest_framework.generics import RetrieveAPIView
from .serializers import GroupMessageRetrieveSerializer
from apps.telegram.models import GroupMessage


class GroupMessageRetrieveApiView(RetrieveAPIView):
    queryset = GroupMessage.objects.all()
    serializer_class = GroupMessageRetrieveSerializer

__all__ = ("GroupMessageRetrieveApiView", )
