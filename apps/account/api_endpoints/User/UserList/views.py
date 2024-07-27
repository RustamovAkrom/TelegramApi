from rest_framework.generics import ListAPIView
from apps.account.models import User
from .serializers import UserListSerializer


class UserListApiView(ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserListSerializer


__all__ = ("UserListApiView",)
