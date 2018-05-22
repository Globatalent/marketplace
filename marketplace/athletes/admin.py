from django.contrib import admin
from marketplace.athletes.models import Athlete, Picture, Link, Review

admin.site.register(Picture)
admin.site.register(Link)
admin.site.register(Review)


class ReviewInLine(admin.TabularInline):
    model = Review
    fields = ('text', 'state',)


@admin.register(Athlete)
class ProjectAdmin(admin.ModelAdmin):
    model = Athlete
    list_display = ('first_name', 'sport', 'state',)
