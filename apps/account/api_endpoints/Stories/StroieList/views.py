from rest_framework.generics import ListAPIView
from apps.account.models import Stories
from .serializers import StorieListSerializer


class StorieListApiView(ListAPIView):
    queryset = Stories.objects.all()
    serializer_class = StorieListSerializer


__all__ = ("StorieListApiView", )