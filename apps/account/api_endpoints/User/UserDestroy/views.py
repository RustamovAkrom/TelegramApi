from rest_framework.generics import DestroyAPIView
from .serializers import UserDestroySerializer
from apps.account.models import User


class UserDestroyApiView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer


__all__ = ("UserDestroyApiView",)
