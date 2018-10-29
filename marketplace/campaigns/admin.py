from django.contrib import admin

from marketplace.campaigns.models import Campaign, Sport, Link, Revenue, Income, Recommendation, Picture, Review


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


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ["id", "kind", "title", "is_draft", "state", "user", "created"]
    list_filter = ["is_draft", "kind", "state", "sport"]
    autocomplete_fields = ["sport", "user", "tags"]
    search_fields = ["user__email", "title", "description", "tags__name", "sport__name"]
    inlines = [LinkInline, PictureInline, RevenueInline, IncomeInline, RecommendationInline, ReviewInLine]
