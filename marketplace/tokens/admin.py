from django.contrib import admin, messages
from django.utils.translation import ugettext_lazy as _

from marketplace.campaigns.helpers import generate_token_code
from marketplace.tokens.models import Token


def regenerate_token_code(modeladmin, request, queryset):
    for token in queryset:
        token.code = generate_token_code(token.campaign.title)
        token.save()
    messages.success(request, _("Codes regenerated!"))

regenerate_token_code.short_description = _("Regenerate token code")


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ["id", "campaign", "amount", "price", "created"]
    actions = [regenerate_token_code]
    search_fields = ["name", "code"]
