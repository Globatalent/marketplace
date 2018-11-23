from django.contrib import admin, messages
from django.utils.translation import ugettext_lazy as _

from marketplace.campaigns.constants import APPROVED
from marketplace.campaigns.models import (
    Campaign,
    Sport,
    Link,
    Revenue,
    Income,
    Recommendation,
    Picture,
    Review,
)


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


class LinkInline(admin.TabularInline):
    model = Link


class PictureInline(admin.TabularInline):
    model = Picture


class RevenueInline(admin.TabularInline):
    model = Revenue


class IncomeInline(admin.TabularInline):
    model = Income


class RecommendationInline(admin.TabularInline):
    model = Recommendation


class ReviewInLine(admin.TabularInline):
    model = Review


def approve_campaigns(modeladmin, request, queryset):
    for campaign in queryset:
        campaign.state = APPROVED
        campaign.save()
    messages.success(request, _("Campaigns approved!"))


approve_campaigns.short_description = _("Approve campaigns")


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ["id", "kind", "title", "is_draft", "state", "user", "country", "created", "started", "finished"]
    list_filter = ["is_draft", "kind", "state", "sport", "country"]
    autocomplete_fields = ["sport", "user", "tags", "token"]
    search_fields = ["user__email", "title", "description", "tags__name", "sport__name"]
    inlines = [
        LinkInline,
        PictureInline,
        RevenueInline,
        IncomeInline,
        RecommendationInline,
        ReviewInLine,
    ]
    actions = [approve_campaigns]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "user",
                    "is_draft",
                    "kind",
                    "state",
                    "rating",
                    "token",
                    "started",
                    "finished",
                    "country",
                ]
            },
        ),
        (
            _("Card"),
            {"fields": ["title", "description", "image", "gender", "sport", "tags"]},
        ),
        (
            _("Content"),
            {
                "fields": [
                    "height",
                    "weight",
                    "club",
                    "coach",
                    "pitch_url",
                    "pitch_image",
                ]
            },
        ),
        (
            _("Career & club"),
            {
                "fields": [
                    "ranking",
                    "biography",
                    "achievements",
                    "history",
                    "players",
                    "expected",
                ]
            },
        ),
        (
            _("Founding"),
            {"fields": ["currency", "funds", "soft_cap", "use", "give_back", "examples"]},
        ),
    ]
