from django.contrib import admin

from .models import RegisteredUser, FeedItem, Ownable


# Register your models here.


@admin.register(RegisteredUser)
class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'show_tracking']

    def show_tracking(self, obj):
        return ', '.join([a.user.username for a in obj.tracking.all()])


@admin.register(FeedItem)
class FeedItemAdmin(admin.ModelAdmin):
    list_display = ['content', 'user']
