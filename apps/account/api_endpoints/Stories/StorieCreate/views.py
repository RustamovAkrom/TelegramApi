from rest_framework.generics import CreateAPIView
from apps.account.models import Stories
from .serializers import StorieCreateSerializer


class StorieCreateApiView(CreateAPIView):
    queryset = Stories.objects.all()
    serializer_class = StorieCreateSerializer


__all__ = ("StorieCreateApiView",)
