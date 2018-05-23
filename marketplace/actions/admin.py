from django.contrib import admin

from marketplace.actions.models import ActionType, Action, Notification

admin.site.register(ActionType)
admin.site.register(Action)
admin.site.register(Notification)
