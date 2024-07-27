from rest_framework.generics import CreateAPIView
from .serializers import GroupCreateSerializer
from apps.telegram.models import Group


class GroupCreateApiView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateSerializer


__all__ = ("GroupCreateApiView",)
