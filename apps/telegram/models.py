from django.db import models
from apps.shared.models import BaseSharedModel


class ChatUser(BaseSharedModel):
    user = models.OneToOneField("account.UserAccount", models.CASCADE, related_name="user_chat")
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=['created_at'])
        ]
        db_table = "chat_users"


class ChatMessage(BaseSharedModel):
    user = models.ForeignKey(ChatUser, models.CASCADE, related_name="user_chat_message")
    message = models.TextField()
    media = models.FileField(upload_to="telegra/chat/messages/%Y/%m/%d", blank=True, null=True)

    def __str__(self) -> str:
        return self.message
    
    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=['created_at'])
        ]
        db_table = "chat_messages"


class Chat(BaseSharedModel):
    user_from = models.ForeignKey(ChatUser, models.CASCADE, related_name="user_from_chat")
    user_to = models.ForeignKey(ChatUser, models.CASCADE, related_name="user_to_chat")

    def __str__(self) -> str:
        return f"{self.user_from} == {self.user_to}"
    
    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=['created_at'])
        ]
        db_table = "chats"


class GroupUser(BaseSharedModel):
    user = models.ForeignKey("account.UserAccount", models.CASCADE, related_name="user_group")
    is_owner = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=['created_at'])
        ]
        db_table = "group_users"


class GroupMessage(BaseSharedModel):
    user = models.ForeignKey(GroupUser, models.CASCADE, related_name="group_user_messages")
    message = models.TextField()
    media = models.FileField(upload_to="telegram/groups/messages/%Y/%m/%d", blank=True, null=True)

    def __str__(self) -> str:
        return self.message
    
    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=['created_at'])
        ]
        db_table = "group_messages"


class Group(BaseSharedModel): 
    photo = models.ImageField(upload_to="telegram/channel/photos/%Y/%m/%d", default="group.jpg", blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150, blank=True, null=True)
    is_public = models.BooleanField(default=False)
    public_link = models.CharField(max_length=120, blank=True, null=True, unique=True)
    private_link = models.CharField(max_length=120, unique=True)
    messages = models.ForeignKey(GroupMessage, models.CASCADE, related_name="message_group", blank=True, null=True)
    users = models.ManyToManyField(GroupUser, related_name="users_group")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=['created_at'])
        ]
        db_table = "groups"

class ChannelUser(BaseSharedModel):
    user = models.ForeignKey("account.UserAccount", models.CASCADE, related_name="user_channel")
    is_owner = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=['created_at'])
        ]
        db_table = "channel_users"



    def __str__(self) -> str:
        return self.message
    
    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=['created_at'])
        ]
        db_table = "channel_messages"


class ChannelStories(BaseSharedModel):
    storie = models.FileField(upload_to="telegram/channel/stories/%Y/%m/%d")
    message = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.storie.url
    
    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=['created_at'])
        ]
        db_table = "channel_stories"


class ChannelDiscusion(BaseSharedModel):
    group = models.ForeignKey(Group, models.CASCADE, related_name="group_channel_discusion")

    def __str__(self) -> str:
        return self.group.name

class ChannelMessage(BaseSharedModel):
    user = models.ForeignKey(ChannelUser, models.CASCADE, related_name="channel_user_messages")
    message = models.TextField()
    media = models.FileField(upload_to="telegram/channel/messages/%Y/%m/%d", blank=True, null=True)
    discusions = models.OneToOneField(ChannelDiscusion, models.CASCADE, related_name="group_discusion_channel_message")
    

class Channel(BaseSharedModel):
    photo = models.ImageField(upload_to="telegram/channel/photos/%Y/%m/%d", default="channel.jpg", blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150,blank=True, null=True)
    public_link = models.CharField(max_length=120)
    messages = models.ForeignKey(ChannelMessage, models.CASCADE, related_name="message_channel", blank=True, null=True)
    users = models.ManyToManyField(ChannelUser, related_name="users_channel")
    stories = models.ManyToManyField(ChannelStories, related_name="stories_channel", blank=True)
    discusions = models.OneToOneField(ChannelDiscusion, models.CASCADE, related_name="discusion_channel")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=['created_at'])
        ]
        db_table = "channels"