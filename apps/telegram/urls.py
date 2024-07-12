from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import IndexView

from .api_endpoints.Channel.Channel import *
from .api_endpoints.Channel.ChannelMessage import *
from .api_endpoints.Channel.ChannelStories import *
from .api_endpoints.Channel.ChannelUser import *

from .api_endpoints.Chat.Chat import *
from .api_endpoints.Chat.ChatMessage import *
from .api_endpoints.Chat.ChatUser import *

from .api_endpoints.Group.Group import *
from .api_endpoints.Group.GroupMessage import *
from .api_endpoints.Group.GroupUser import *


app_name = "telegram"

urlpatterns = [
    # Home url
    path(_(""), IndexView.as_view(), name="home"),
    # Channel urls
    path(_("channel-create/"), ChannelCreateApiView.as_view(), name="channel-create"),
    path(_("channel-list/"), ChannelListApiView.as_view(), name="channel-list"),
    path(_("channel-retrieve/<int:pk>",), ChannelRetrieveApiView.as_view(), name="channel-retrieve"),
    path(_("channel-update/<int:pk>"), ChannelUpdateApiView.as_view(),name="channel-update"),
    path(_("channel-destroy/<int:pk>"), ChannelDestroyApiView.as_view(),name="channel-destroy"),
    # Channel Message urls
    path(_("channel-message-create/"), ChannelMessageCreateApiView.as_view(), name="channel-message-create"),
    path(_("channel-message-list/"), ChannelMessageListApiView.as_view(), name="channel-message-list"),
    path(_("channel-message-retrieve/<int:pk>"), ChannelMessageRetrieveApiView.as_view(), name="channel-message-retrieve"),
    path(_("channel-message-update/i<int:pk>"), ChannelMessageUpdateApiView.as_view(), name="channel-message-update"),
    path(_("channel-message-destroy/<int:pk>"), ChannelMessageDestroyApiView.as_view(), name="channel-message-destroy"),
    # Channel Storie urls
    path(_("channel-storie-create/"), ChannelStorieCreateApiView.as_view(), name="channel-storie-create"),
    path(_("channel-storie-list/"), ChannelStorieListApiView.as_view(), name="channel-storie-list"),
    path(_("channel-storie-retrieve/<int:pk>"), ChannelStorieRetriveApiView.as_view(), name="channel-storie-retrieve"),
    path(_("channel-storie-update/<int:pk>"), ChannelStoriesUpdateApiView.as_view(), name="channel-storie-update"),
    path(_("channel-storie-destroy/<int:pk>"), ChannelStorieDestroyApiView.as_view(), name="channel-storie-destroy"),
    # Channel User urls
    path(_("channel-user-create/"), ChannelUserCreateApiView.as_view(), name="channel-user-create"),
    path(_("channel-user-list/"), ChannelUserListApiView.as_view(), name="channel-user-list"),
    path(_("channel-user-retrieve/<int:pk>"), ChannelUserRetrieveApiView.as_view(), name="channel-user-retrieve"),
    path(_("channel-user-update/<int:pk>"), ChannelUserUpdateApiView.as_view(), name="channel-user-update"),
    path(_("channel-user-destroy/<int:pk>"), ChannelUserDestroyApiView.as_view(), name="channel-user-destroy"),
    # Group urls
    path(_("group-create/"), GroupCreateApiView.as_view(), name="group-create"),
    path(_("group-list/"), GroupListApiView.as_view(), name="group-list"),
    path(_("group-retrieve/<int:pk>"), GroupRetrieveApiView.as_view(), name="group-retrieve"),
    path(_("group-update/<int:pk>"), GroupUpdateApiView.as_view(), name="group-update"),
    path(_("group-destroy/<int:pk>"), GroupDestroyApiView.as_view(), name="group-destroy"),
    # Group Message urls
    path(_("group-message-create/"), GroupMessageCreateApiView.as_view(), name="group-message-create"),
    path(_("group-message-list/"), GroupMessageListApiView.as_view(), name="group-message-list"),
    path(_("group-message-retrieve/<int:pk>"), GroupMessageRetrieveApiView.as_view(), name="group-message-retrive"),
    path(_("group-message-update/<int:pk>"), GroupMessageUpdateApiView.as_view(), name="group-message-update"),
    path(_("group-message-destroy/<int:pk>"), GroupMessageDestroyApiView.as_view(), name="group-message-destroy"),
    # Group User urls
    path(_("group-user-create/"), GroupUserCreateApiView.as_view(), name="group-user-create"),
    path(_("group-user-list/"), GroupUserListApiView.as_view(), name="group-user-list"),
    path(_("group-user-retrieve/<int:pk>"), GroupUserRetrieveApiView.as_view(), name="group-user-retrieve"),
    path(_("group-user-update/<int:pk>"), GroupUserUpdateApiView.as_view(), name="group-user-update"),
    path(_("group-user-destroy/<int:pk>"), GroupUserDestroyApiView.as_view(), name="group-user-destroy"),
    # Chat urls
    path(_("chat-create/"), ChatCreateApiView.as_view(), name="chat-create"),
    path(_("chat-list/"), ChatListApiView.as_view(), name="chat-list"),
    path(_("chat-retrive/<int:pk>"), ChatRetrieveApiView.as_view(), name="chat-retrieve"),
    path(_("chat-update/<int:pk>"), ChatUpdateApiView.as_view(), name="chat-update"),
    path(_("chat-destroy/<int:pk>"), ChatDestroyApiView.as_view(), name="chat-destroy"),
    # Chat Message urls
    path(_("chat-message-create/"), ChatMessageCreateApiView.as_view(), name="chat-message-create"), 
    path(_("chat-message-list/"), ChatMessageListApiView.as_view(), name="chat-message-list"), 
    path(_("chat-message-retrieve/<int:pk>"), ChatMessageRetrieveApiView.as_view(), name="chat-message-retrieve"), 
    path(_("chat-message-update/<int:pk>"), ChatMessageUpdateApiView.as_view(), name="caht-message-update"), 
    path(_("chat-message-destroy/<int:pk>"), ChatMessageDestroyApiView.as_view(), name="chat-message-destroy"), 
    # Chat User urls
    path(_("chat-user-create/"), ChatUserCreateApiView.as_view(), name="chat-user-create"),
    path(_("chat-user-list/"), ChatUserListApiView.as_view(), name="chat-user-list"),
    path(_("chat-user-retrieve/<int:pk>"), ChatUserRetrieveApiView.as_view(), name="chat-user-retrieve"),
    path(_("chat-user-update/<int:pk>"), ChatUserUpdateApiView.as_view(), name="chat-user-update"),
    path(_("chat-user-destroy/<int:pk>"), ChatUserDestroyApiView.as_view()),

]
