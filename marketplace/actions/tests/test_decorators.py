from test_plus.test import TestCase

from marketplace.actions.models import Action, Notification
from marketplace.campaigns.tests.factories import CampaignFactory
from marketplace.purchases.tests.factories import PurchaseFactory
from marketplace.tokens.tests.factories import TokenFactory
from marketplace.users.tests.factories import UserFactory


class ActionsDecoratorsTests(TestCase):
    user_factory = UserFactory

    def setUp(self):
        self.user = self.make_user()

    def test_decorate_follow(self):
        self.assertEqual(0, Action.objects.all().count())
        self.assertEqual(0, Notification.objects.all().count())

        user = UserFactory()
        campaign = CampaignFactory()
        # .follow() is decorated
        user.follow(campaign)

        self.assertEqual(1, Action.objects.all().count())
        self.assertEqual(1, Notification.objects.all().count())
        notification = Notification.objects.last()
        self.assertEqual(notification.user, campaign.user)

    def test_decorate_add_purchase(self):
        self.assertEqual(0, Action.objects.all().count())
        self.assertEqual(0, Notification.objects.all().count())

        campaign = CampaignFactory()
        user = UserFactory()
        token = TokenFactory(campaign=campaign, amount=1000, price=1000)
        PurchaseFactory(token=token, user=user, amount=10)

        self.assertEqual(1, Action.objects.all().count())
        self.assertEqual(1, Notification.objects.filter(user=campaign.user).count())
        notification = Notification.objects.filter(user=campaign.user).last()
        self.assertEqual(notification.user, campaign.user)
