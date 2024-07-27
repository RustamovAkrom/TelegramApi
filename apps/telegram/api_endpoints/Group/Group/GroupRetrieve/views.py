from rest_framework.generics import RetrieveAPIView
from .serializers import GroupRetrieveSerializer
from apps.telegram.models import Group


class GroupRetrieveApiView(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupRetrieveSerializer


__all__ = ("GroupRetrieveApiView",)
