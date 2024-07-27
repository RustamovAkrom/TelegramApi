from rest_framework.generics import UpdateAPIView
from apps.account.models import Stories
from .serializers import StorieUpdateSerializer


class StorieUpdateApiView(UpdateAPIView):
    queryset = Stories.objects.all()
    serializer_class = StorieUpdateSerializer


__all__ = ("StorieUpdateApiView",)
