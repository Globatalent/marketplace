from django.contrib import admin

from marketplace.purchases.models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ["id", "token", "user", "amount", "total", "status", "created"]
