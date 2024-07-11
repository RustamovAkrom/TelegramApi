from django.urls import path
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .api_endpoints.SavedMessages import *
from .api_endpoints.Stories import *
from .api_endpoints.User import *
from .api_endpoints.UserAccount import *


app_name = "account"

urlpatterns = [
    # Jwt Authentifications
    path(_("token/"), TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path(_("token/refresh/"), TokenRefreshView.as_view(), name="token-refresh"),
    # Saved Messages
    path(_("saved-message-create/"), SavedMessageCreateApiView.as_view(), name='saved-message-create'),
    path(_("saved-message-destroy/<int:pk>"), SavedMessageDestroyApiView.as_view(), name="saved-message-destroy"),
    path(_("saved-message-list/"), SavedMessageListAPiView.as_view(), name="saved-message-list"),
    path(_("saved-message-retrive/<int:pk>"), SavedMessageRetriveApiView.as_view(), name="saved-message-retrive"),
    path(_("saved-message-update/<int:pk>"), SavedMessageUpdateApiView.as_view(), name="saved-message-update"),
    # Stories
    path(_("storie-create/"), StorieCreateApiView.as_view(), name="storie-create"),
    path(_("storie-destroy/<int:pk>"), StorieDestroyApiView.as_view(), name="storie-destroy"),
    path(_("storie-retrive/<int:pk>"), StorieRetriveApiView.as_view(), name="storie-retrive"),
    path(_("storie-update/<int:pk>"), StorieUpdateApiView.as_view(), name="storie-update"),
    path(_("storie-list"), StorieListApiView.as_view(), name="storie-list"),
    # User,
    path(_("user-activate/"), UserActivateApiView.as_view(), name="user-activate"),
    path(_("user-create/"), UserCreateApiView.as_view(), name="user-create"),
    path(_("user-list/"), UserListApiView.as_view(), name="user-list"),
    path(_("user-destroy/<int:pk>"), UserDestroyApiView.as_view(), name="user-destroy"),
    # UserAccount
    path(_("user-account-create/"), UserAccountCreateApiView.as_view(), name="user-account-create"),
    path(_("user-account-destroy/<int:pk>"), UserAccountDestroyApiView.as_view(), name="user-account-destroy"),
    path(_("user-account-retrive/<int:pk>"), UserAccountRetriceApiView.as_view(), name="user-account-retrive"),
    path(_("user-account-update/<int:pk>"), UserAccountUpdateApiView.as_view(), name="user-account-update"),
    path(_("user-account-list/"), UserAccountListApiView.as_view(), name="user-account-list"),
]
