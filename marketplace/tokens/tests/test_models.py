from django.db import IntegrityError
from test_plus.test import TestCase

from marketplace.users.tests.factories import UserFactory
from marketplace.tokens.tests.factories import TokenFactory
from marketplace.supporters.tests.factories import SupporterFactory
from marketplace.tokens.models import Purchase


class PurchasesTests(TestCase):
    user_factory = UserFactory

    def setUp(self):
        self.user = self.make_user()

    def test_purchase(self):
        token = TokenFactory(amount=100000, price=100000)
        purchase = Purchase(token=token, amount=token.amount / 2, supporter=SupporterFactory())
        try:
            purchase.save()
            raised_exception = False
        except IntegrityError:
            raised_exception = True
        self.assertFalse(raised_exception)
        self.assertAlmostEqual(purchase.total, token.unit_price() * purchase.amount)

    def test_purchase_amount_limit(self):
        token = TokenFactory(amount=100000, price=100000)
        purchase = Purchase(token=token, amount=token.amount + 1, supporter=SupporterFactory())
        try:
            purchase.save()
            raised_exception = False
        except IntegrityError:
            raised_exception = True
        self.assertTrue(raised_exception)

