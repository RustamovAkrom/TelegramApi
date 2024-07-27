from rest_framework.generics import DestroyAPIView
from apps.account.models import Stories
from .serializers import StorieDestroySerializer


class StorieDestroyApiView(DestroyAPIView):
    queryset = Stories.objects.all()
    serializer_class = StorieDestroySerializer


__all__ = ("StorieDestroyApiView",)
