from django.contrib import admin

from marketplace.campaigns.models import Campaign, Sport, Link, Revenue, Income, Recommendation, Picture


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


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ["id", "kind", "title", "is_draft", "user", "created"]
    list_filter = ["is_draft", "kind"]
    autocomplete_fields = ["sport", "user", "tags"]
    search_fields = ["user__email", "title"]
    inlines = [LinkInline, PictureInline, RevenueInline, IncomeInline, RecommendationInline]
