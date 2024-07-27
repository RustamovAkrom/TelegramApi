from rest_framework.generics import UpdateAPIView
from .serializers import GroupUserUpdateSerializer
from apps.telegram.models import GroupUser


class GroupUserUpdateApiView(UpdateAPIView):
    queryset = GroupUser.objects.all()
    serializer_class = GroupUserUpdateSerializer


__all__ = ("GroupUserUpdateApiView",)
