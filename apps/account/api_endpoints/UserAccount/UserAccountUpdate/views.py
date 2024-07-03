from rest_framework.generics import UpdateAPIView
from apps.account.models import UserAccount
from .serializers import UserAccountUpdateSerializer


class UserAccountUpdateApiView(UpdateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountUpdateSerializer


__all__ = ("UserAccountUpdateApiView", )