from django.contrib import admin
from .models import Stories, UserAccount, User, SavedMessages


@admin.register(Stories)
class StoriesAdmin(admin.ModelAdmin):
    pass

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "phone_number", "date_of_berth", "stories"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(SavedMessages)
class SavedMessagesAdmin(admin.ModelAdmin):
    pass
