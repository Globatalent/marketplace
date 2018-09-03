from django.utils.translation import ugettext_lazy as _


PAID, PENDING, CANCELED = 'paid', 'pending', 'canceled'
STATUS_CHOICES = (
    (PAID, 'Paid'),
    (PENDING, 'Pending'),
    (CANCELED, 'Cancelled'),
)

EUR, USD, ETH, BTC = "EUR", "USD", "ETH", "BTC"
CURRENCY_CHOICES = (
    (EUR, _('EUR')),
    (USD, _('USD')),
    (ETH, _('ETH')),
    (BTC, _('BTC')),
)
