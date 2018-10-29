from django.contrib import admin

from marketplace.tokens.models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ["id", "campaign", "amount", "price", "created"]
