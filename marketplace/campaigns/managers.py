import datetime

from django.db import models
from django.db.models import Q

from marketplace.campaigns.constants import APPROVED


class CampaignQuerySet(models.QuerySet):

    def search(self, query):
        """Query set to handle search."""
        return self.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(sport__name__icontains=query) |
            Q(tags__name__icontains=query)
        )

    def active(self):
        """Returns active campaigns"""
        return self.filter(
            is_draft=False,
            state=APPROVED,
            finished__isnull=False,
            finished__gte=datetime.date.today()
        )

    def inactive(self):
        """Returns inactive campaigns"""
        return self.filter(
            is_draft=False,
            state=APPROVED,
            finished__isnull=False,
            finished__lt=datetime.date.today()
        )


CampaignManager = CampaignQuerySet.as_manager
