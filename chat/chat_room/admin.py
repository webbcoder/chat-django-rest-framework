from django.contrib import admin
from .models import Room, Chat

# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    list_display = ('creator', 'invited_user', 'date')

    def invited_user(self, obj):
        return "\n".join([user.username for user in obj.invited.all()])


class ChatAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'text', 'date')


admin.site.register(Chat, ChatAdmin)
admin.site.register(Room, RoomAdmin)
