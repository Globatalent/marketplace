from django.db import IntegrityError
from test_plus.test import TestCase

from marketplace.campaigns.tests.factories import CampaignFactory
from marketplace.purchases.models import Purchase
from marketplace.users.tests.factories import UserFactory


class PurchasesTests(TestCase):
    user_factory = UserFactory

    def setUp(self):
        self.user = self.make_user()

    def test_purchase(self):
        campaign = CampaignFactory(is_draft=False, funds=100000)
        token = campaign.token
        purchase = Purchase(token=token, amount=token.amount / 2, user=UserFactory())
        try:
            purchase.save()
            raised_exception = False
        except IntegrityError:
            raised_exception = True
        self.assertFalse(raised_exception)
        self.assertAlmostEqual(purchase.total, token.unit_price * purchase.amount)

    def test_purchase_amount_limit(self):
        campaign = CampaignFactory(is_draft=False, funds=100000)
        token = campaign.token
        purchase = Purchase(token=token, amount=token.amount + 1, user=UserFactory())
        try:
            purchase.save()
            raised_exception = False
        except IntegrityError:
            raised_exception = True
        self.assertTrue(raised_exception)
