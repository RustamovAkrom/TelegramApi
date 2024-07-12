from rest_framework.generics import RetrieveAPIView
from .serializers import GroupUserRetrieveSerializer
from apps.telegram.models import GroupUser


class GroupUserRetrieveApiView(RetrieveAPIView):
    queryset = GroupUser.objects.all()
    serializer_class = GroupUserRetrieveSerializer

__all__ = ("GroupUserRetrieveApiView", )
