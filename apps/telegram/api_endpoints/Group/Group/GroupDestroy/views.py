from rest_framework.generics import DestroyAPIView
from .serializers import GroupDestroySerializer
from apps.telegram.models import Group


class GroupDestroyApiView(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupDestroySerializer

__all__ = ("GroupDestroyApiView", )
