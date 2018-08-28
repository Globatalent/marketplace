from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Sum
from django.db import IntegrityError

from model_utils.models import TimeStampedModel


class Token(TimeStampedModel):
    """Token created by the athlete."""
    athlete = models.ForeignKey("athletes.Athlete", related_name="tokens", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(help_text=_("amount of tokens issued by the athlete"))
    price = models.FloatField(help_text=_("total price for the amount of tokens issued"))

    class Meta:
        ordering = ("created", )

    @property
    def unit_price(self):
        """Price for single token."""
        return self.price / self.amount

    @property
    def remaining(self):
        """Remaining amount of tokens."""
        return self.amount - (self.purchases.aggregate(total_amount=Sum('amount')).get('total_amount', 0) or 0)

    def save(self, *args, **kwargs):
        if self.amount <= 0:
            raise IntegrityError("amount field should be greater than 0")
        return super().save(*args, **kwargs)


class Purchase(TimeStampedModel):
    """A purchase from a supporter of an amount of tokens from an athlete."""
    supporter = models.ForeignKey("supporters.Supporter", related_name="purchases", on_delete=models.CASCADE)
    token = models.ForeignKey("tokens.Token", related_name="purchases", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(help_text=_("amount of tokens purchaed by the supporter"))
    total = models.FloatField(help_text=_("total paid for the amount of tokens"))

    class Meta:
        ordering = ("created", )

    def save(self, *args, **kwargs):
        is_insert = self.pk is None
        if self.amount > self.token.remaining:
            raise IntegrityError("You can't purchase more than the remaining tokens")
        if is_insert and not self.total and self.token:
            self.total = self.token.unit_price * self.amount
        return super().save(*args, **kwargs)
