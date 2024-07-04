from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from .models import Stories, UserAccount, User, SavedMessages


@admin.register(Stories)
class StoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "phone_number", "date_of_berth", "get_avatar"]
    search_fields = ("username", "first_name", "last_name", "phone_number", "date_of_berth", )
    fields = ("user", "avatar","get_avatar", "bio", "first_name", "last_name", "phone_number", "date_of_berth", "stories")
    readonly_fields = ("get_avatar", )
    list_per_page = 12
    save_on_top = True

    def get_avatar(self, object):
        if object.avatar:
            return mark_safe(f"<img src='{object.avatar.url}' width=50 style='border-radius: 50%;'>")

    get_avatar.short_description = _("Photo")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "phone_number", "is_active"]
    search_fields = ("username", "phone_number", )
    search_help_text = _("Username or phone number")
    list_per_page = 12
    fields = ("password", "last_login", "is_superuser", "user_permissions", "username", "first_name", "last_name", "email", "is_staff", "date_joined", "token", "is_active", "phone_number")
    readonly_fields = ("last_login", "date_joined", )
    save_on_top = True


@admin.register(SavedMessages)
class SavedMessagesAdmin(admin.ModelAdmin):
    list_display = ['message']
    search_fields = ("message", )
    list_per_page = 12
    save_on_top = True

