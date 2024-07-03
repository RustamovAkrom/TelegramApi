from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Chat, ChatUser, ChatMessage, Group, GroupUser, GroupMessage, Channel, ChannelUser, ChannelMessage, ChannelStories


admin.site.register(Chat)
admin.site.register(ChatUser)
admin.site.register(ChatMessage)
admin.site.register(GroupUser)
admin.site.register(GroupMessage)
admin.site.register(ChannelUser)
admin.site.register(ChannelMessage)
admin.site.register(ChannelStories)


@admin.register(Group)
class GroupAdmin(TranslationAdmin):
    pass


@admin.register(Channel)
class ChannelAdmin(TranslationAdmin):
    pass
