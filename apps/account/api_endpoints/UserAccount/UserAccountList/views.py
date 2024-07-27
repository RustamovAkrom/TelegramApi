from rest_framework.generics import ListAPIView
from apps.account.models import UserAccount
from .serializers import UserAccountlistSerializer


class UserAccountListApiView(ListAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountlistSerializer


__all__ = ("UserAccountListApiView",)
