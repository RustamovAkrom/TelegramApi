from rest_framework.generics import ListAPIView
from apps.account.models import SavedMessages
from .serializers import SavedMessageListSerializer


class SavedMessageListAPiView(ListAPIView):
    queryset = SavedMessages.objects.all()
    serializer_class = SavedMessageListSerializer


__all__ = ("SavedMessageListAPiView",)
