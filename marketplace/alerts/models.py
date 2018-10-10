from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from marketplace.alerts.constants import RULE_CHOICES, UP


class Alert(TimeStampedModel):
    rule = models.CharField(choices=RULE_CHOICES, default=UP, max_length=10, verbose_name=_('rule'))
    amount = models.FloatField(verbose_name=_('amount'))
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='alerts',
        on_delete=models.CASCADE
    )
    campaign = models.ForeignKey(
        "campaigns.Campaign",
        related_name='alerts',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('-created', )
