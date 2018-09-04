from django.db import IntegrityError
from django.db import models
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from marketplace.purchases.constants import PAID, CURRENCY_CHOICES, USD


class Token(TimeStampedModel):
    """Token created by the athlete."""
    athlete = models.ForeignKey("athletes.Athlete", related_name="tokens", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=16, null=True, blank=True)
    amount = models.PositiveIntegerField(help_text=_("amount of tokens issued by the athlete"))
    price = models.FloatField(help_text=_("total price for the amount of tokens issued"))
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=USD, blank=True)

    class Meta:
        ordering = ("created", )

    @property
    def unit_price(self):
        """Price for single token."""
        return self.price / self.amount

    @property
    def remaining(self):
        """Remaining amount of tokens."""
        return self.amount - (
            self.purchases.filter(status=PAID).aggregate(total_amount=Sum('amount')).get('total_amount', 0) or 0
        )

    @property
    def progression(self):
        return 1.0 - (self.remaining / self.amount)

    def __str__(self):
        return "{} token: {}".format(str(self.athlete), self.code)

    def save(self, *args, **kwargs):
        if self.amount <= 0:
            raise IntegrityError("amount field should be greater than 0")
        return super().save(*args, **kwargs)
