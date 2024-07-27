from rest_framework.generics import CreateAPIView
from apps.account.models import UserAccount
from .serializers import UserAccountCreateSerializer


class UserAccountCreateApiView(CreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountCreateSerializer

    def get_queryset(self):

        return super().get_queryset()


__all__ = ("UserAccountCreateApiView",)
