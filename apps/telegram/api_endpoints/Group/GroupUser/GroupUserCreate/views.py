from rest_framework.generics import CreateAPIView
from .serializers import GroupUserCreateSerializer
from apps.telegram.models import GroupUser


class GroupUserCreateApiView(CreateAPIView):
    queryset = GroupUser.objects.all()
    serializer_class = GroupUserCreateSerializer

__all__ = ("GroupUserCreateApiView", )
