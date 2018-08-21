from django.contrib import admin

from marketplace.actions.models import Action, Notification

admin.site.register(Action)
admin.site.register(Notification)
