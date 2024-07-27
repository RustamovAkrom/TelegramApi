from rest_framework.generics import RetrieveAPIView
from apps.account.models import UserAccount
from .serializers import UserAccountRetriveSerializer


class UserAccountRetriceApiView(RetrieveAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountRetriveSerializer


__all__ = ("UserAccountRetriceApiView",)
