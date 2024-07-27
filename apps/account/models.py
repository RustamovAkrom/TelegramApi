from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from apps.shared.models import BaseSharedModel
from phonenumber_field.modelfields import PhoneNumberField
from config import settings


class Stories(BaseSharedModel):
    storie = models.FileField(
        _("stories"),
        upload_to="usr/account/stories/%Y/%m/%d",
        help_text=_("Required. stories"),
    )
    message = models.CharField(_("messages"), max_length=120, blank=True, null=True)

    def __str__(self):
        return self.storie.url

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["created_at"])]
        db_table = "stories"
        verbose_name = _("storie")
        verbose_name_plural = _("stories")


class UserAccount(BaseSharedModel):
    user = models.ForeignKey(
        "account.User", models.DO_NOTHING, related_name="user_account"
    )
    avatar = models.ImageField(
        _("avatar"), upload_to="usr/account/avatars/%Y/%m/%d", blank=True, null=True
    )
    bio = models.CharField(_("bio"), max_length=70, blank=True, null=True)
    first_name = models.CharField(_("first name"), max_length=70, blank=True, null=True)
    last_name = models.CharField(_("last name"), max_length=70, blank=True, null=True)
    phone_number = PhoneNumberField(
        _("phone number"), unique=True, region=settings.PHONENUMBER_REGION
    )
    username = models.CharField(_("username"), max_length=120)
    date_of_berth = models.DateField(_("date of berth"), blank=True, null=True)
    stories = models.ManyToManyField(
        Stories, related_name="stories_user_account", blank=True
    )
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)

    def save(self, *args, **kwargs):
        if str(self.username[0]) != "@":
            self.username = f"@{self.username}"
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["created_at"])]
        db_table = "user_accounts"
        verbose_name = _("user account")
        verbose_name_plural = _("user accounts")


class User(AbstractUser):
    token = models.CharField(_("token"), max_length=200, blank=True, null=True)
    is_active = models.BooleanField(_("is active"), default=False)
    phone_number = PhoneNumberField(
        _("phone number"), unique=True, region=settings.PHONENUMBER_REGION
    )

    def __str__(self) -> str:
        return self.username


class SavedMessages(BaseSharedModel):
    user = models.ForeignKey(
        UserAccount, models.CASCADE, related_name="user_saved_messages"
    )
    message = models.TextField(_("message"))

    def __str__(self):
        return f"Saved Message( {self.user} )"

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["created_at"])]
        db_table = "saved_messages"
        verbose_name = _("saved message")
        verbose_name_plural = _("saved messages")
