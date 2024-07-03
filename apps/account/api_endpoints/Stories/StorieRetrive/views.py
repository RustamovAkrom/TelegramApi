from rest_framework.generics import RetrieveAPIView
from apps.account.models import Stories
from .serializers import StorieRetriveSerializer


class StorieRetriveApiView(RetrieveAPIView):
    queryset = Stories.objects.all()
    serializer_class = StorieRetriveSerializer

__all__ = ("StorieRetriveApiView", )