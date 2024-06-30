from django.contrib import admin
from .models import Chat, ChatUser, ChatMessage, Group, GroupUser, GroupMessage, Channel, ChannelUser, ChannelMessage, ChannelStories

admin.site.register(Chat)
admin.site.register(ChatUser)
admin.site.register(ChatMessage)
admin.site.register(Group)
admin.site.register(GroupUser)
admin.site.register(GroupMessage)
admin.site.register(Channel)
admin.site.register(ChannelUser)
admin.site.register(ChannelMessage)
admin.site.register(ChannelStories)