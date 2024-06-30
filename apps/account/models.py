from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.core.exceptions import ValidationError
from apps.shared.models import BaseSharedModel

# from phonenumber_field.modelfields import PhoneNumberField
from config import settings


class Stories(BaseSharedModel):
    storie = models.FileField(upload_to="usr/account/stories/%Y/%m/%d")
    message = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.storie.url
    
    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=['created_at'])
        ]
        db_table = "stories"

    
class UserAccount(BaseSharedModel):
    avatar = models.ImageField(upload_to="usr/account/avatars/%Y/%m/%d", blank=True, null=True)
    bio = models.CharField(max_length=70, blank=True, null=True)
    first_name = models.CharField(max_length=70, blank=True, null=True)
    last_name = models.CharField(max_length=70, blank=True, null=True)
    phone_number = models.CharField(max_length=14) #region=settings.PHONENUMBER_REGION)
    username = models.CharField(max_length=120)
    date_of_berth = models.DateField(blank=True, null=True)
    stories = models.ForeignKey(Stories, models.CASCADE, related_name="stories_user_account", blank=True, null=True)

    def __str__(self):
        return str(self.username)
    
    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=['created_at'])
        ]
        db_table = "user_accounts"


class User(AbstractUser):
    phone_number = models.CharField(unique=True, max_length=14) #region=settings.PHONENUMBER_REGION)
    account = models.ForeignKey(UserAccount, models.DO_NOTHING, related_name="account_user", blank=True)

    def save(self, *args, **kwargs) -> None:
        account = UserAccount.objects.create(username = self.username, phone_number = self.phone_number)
        self.account = account
        
        return super().save(*args, **kwargs)
    

    def __str__(self) -> str:
        return self.username


class SavedMessages(BaseSharedModel):
    user = models.ForeignKey(UserAccount, models.CASCADE, related_name="user_saved_messages")
    message = models.TextField()

    def __str__(self):
        return f"Saved Message( {self.user} )"
      
    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=['created_at'])
        ]
        db_table = "saved_messages"
