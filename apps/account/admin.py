from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Stories, UserAccount, User, SavedMessages


@admin.register(Stories)
class StoriesAdmin(admin.ModelAdmin):
    pass

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "phone_number", "date_of_berth"]
    search_fields = ("username", "first_name", "last_name", "phone_number", "date_of_berth", )
    list_per_page = 12


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "phone_number", "is_active"]
    search_fields = ("username", "phone_number", )
    search_help_text = _("Username or phone number")
    list_per_page = 12
    

@admin.register(SavedMessages)
class SavedMessagesAdmin(admin.ModelAdmin):
    list_display = ['message']
    search_fields = ("message", )
    list_per_page = 12
    