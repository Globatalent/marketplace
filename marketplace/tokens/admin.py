from django.contrib import admin

from marketplace.tokens.models import Token
from marketplace.tokens.models import Purchase


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ["id", "athlete", "amount", "price", "created"]


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ["id", "token", "amount", "total", "status", "created"]
