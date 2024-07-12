from rest_framework.generics import DestroyAPIView
from .serializers import GroupUserDestroySerializer
from apps.telegram.models import GroupUser


class GroupUserDestroyApiView(DestroyAPIView):
    queryset = GroupUser.objects.all()
    serializer_class = GroupUserDestroySerializer

__all__ = ("GroupUserDestroyApiView", )
