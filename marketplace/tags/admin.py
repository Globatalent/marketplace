from django.contrib import admin

from marketplace.tags.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created"]
    search_fields = ["name"]
