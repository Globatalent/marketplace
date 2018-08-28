from django.contrib import admin
from marketplace.athletes.models import Athlete, Picture, Link, Review

admin.site.register(Picture)
admin.site.register(Link)
admin.site.register(Review)


class ReviewInLine(admin.TabularInline):
    model = Review
    fields = ('text', 'state',)


class PictureInline(admin.TabularInline):
    model = Picture
    fields = ('image',)


class LinkInline(admin.TabularInline):
    model = Link
    fields = ('name', 'url')


@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'sport', 'state',)
    inlines = [PictureInline, LinkInline]
