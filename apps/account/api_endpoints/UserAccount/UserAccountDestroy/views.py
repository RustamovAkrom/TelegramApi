from rest_framework.generics import DestroyAPIView
from apps.account.models import UserAccount
from .serializers import UserAccountDestroySerializer


class UserAccountDestroyApiView(DestroyAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountDestroySerializer

__all__ = ("UserAccountDestroyApiView", )