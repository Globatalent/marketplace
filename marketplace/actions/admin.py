from django.contrib import admin

from marketplace.actions.models import Action, Notification


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ["id", "actor", "verb", "trigger", "target", "send", "created"]


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "action", "read", "read_at", "created"]

