from rest_framework.generics import ListAPIView
from .serializers import GroupUserListSerializer
from apps.telegram.models import GroupUser


class GroupUserListApiView(ListAPIView):
    queryset = GroupUser.objects.all()
    serializer_class = GroupUserListSerializer

__all__ = ("GroupUserListApiView", )
