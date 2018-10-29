from django.db import models
from django.db.models import Q


class CampaignQuerySet(models.QuerySet):
    """Query set to handle search."""

    def search(self, query):
        return self.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(sport__name__icontains=query) |
            Q(tags__name__icontains=query)
        )


CampaignManager = CampaignQuerySet.as_manager
