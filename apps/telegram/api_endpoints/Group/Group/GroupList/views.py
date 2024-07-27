from rest_framework.generics import ListAPIView
from .serializers import GroupListSerializer
from apps.telegram.models import Group


class GroupListApiView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer


__all__ = ("GroupListApiView",)
