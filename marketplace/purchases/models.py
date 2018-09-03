from django.db import IntegrityError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from marketplace.actions.constants import PURCHASE
from marketplace.actions.decorators import dispatch_action
from marketplace.athletes.constants import APPROVED
from marketplace.purchases.constants import STATUS_CHOICES, PENDING


class Purchase(TimeStampedModel):
    """A purchase from a supporter of an amount of tokens from an athlete."""
    supporter = models.ForeignKey("supporters.Supporter", related_name="purchases", on_delete=models.CASCADE)
    token = models.ForeignKey("tokens.Token", related_name="purchases", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(help_text=_("amount of tokens purchased by the supporter"))
    total = models.FloatField(blank=True, help_text=_("total paid for the amount of tokens"))
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=PENDING, blank=True)

    class Meta:
        ordering = ("created", )

    @dispatch_action(PURCHASE, method=True)
    def save(self, *args, **kwargs):
        is_insert = self.pk is None
        if self.amount > self.token.remaining:
            raise IntegrityError("You can't purchase more than the remaining tokens")
        if self.token.athlete.state != APPROVED:
            raise IntegrityError("You can't purchase tokens from an unapproved athlete")
        if is_insert and not self.total and self.token:
            self.total = self.token.unit_price * self.amount
        return super().save(*args, **kwargs)
