from django.contrib import admin

from marketplace.alerts.models import Alert


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ["id", "rule", "amount", "campaign", "user", "created"]
