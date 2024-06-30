from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .api_endpoints.SavedMessages import *


app_name = "account"
urlpatterns = [
    # Jwt Authentifications
    path("token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    # Saved Messages
    path("saved-message-create/", SavedMessageCreateApiView.as_view(), name='saved-message-create'),
    path("saved-message-destroy/<int:pk>/", SavedMessageDestroyApiView.as_view(), name="saved-message-destroy"),
    path("saved-message-list/", SavedMessageListAPiView.as_view(), name="saved-message-list"),
    path("saved-message-retrive/<int:pk>", SavedMessageRetriveApiView.as_view(), name="saved-message-retrive"),
    path("saved-message-update/<int:pk>", SavedMessageUpdateApiView.as_view(), name="saved-message-update")
]