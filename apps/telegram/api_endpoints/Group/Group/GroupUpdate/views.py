from rest_framework.generics import UpdateAPIView
from .serializers import GroupUpdateSerializer
from apps.telegram.models import Group


class GroupUpdateApiView(UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupUpdateSerializer


__all__ = ("GroupUpdateApiView",)
