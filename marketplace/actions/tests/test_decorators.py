from test_plus.test import TestCase

from marketplace.athletes.tests.factories import PictureFactory, ReviewFactory
from marketplace.actions.models import Action, Notification
from marketplace.athletes.tests.factories import AthleteFactory
from marketplace.purchases.tests.factories import PurchaseFactory
from marketplace.supporters.tests.factories import SupporterFactory
from marketplace.tokens.tests.factories import TokenFactory
from marketplace.users.tests.factories import UserFactory


class ActionsDecoratorsTests(TestCase):
    user_factory = UserFactory

    def setUp(self):
        self.user = self.make_user()

    def test_decorate_follow(self):
        self.assertEqual(0, Action.objects.all().count())
        self.assertEqual(0, Notification.objects.all().count())

        supporter = SupporterFactory()
        athlete = AthleteFactory()
        # .follow() is decorated
        supporter.follow(athlete)

        self.assertEqual(1, Action.objects.all().count())
        self.assertEqual(1, Notification.objects.all().count())
        notification = Notification.objects.last()
        self.assertEqual(notification.user, athlete.user)

    def test_decorate_add_picture(self):
        self.assertEqual(0, Action.objects.all().count())
        self.assertEqual(0, Notification.objects.all().count())

        # Supporter follows athlete
        supporter = SupporterFactory()
        athlete = AthleteFactory()
        supporter.follow(athlete)

        # Athlete add a new picture
        PictureFactory(athlete=athlete)

        self.assertEqual(2, Action.objects.all().count())  # Two actions, follows and adds a picture
        self.assertEqual(1, Notification.objects.filter(user=supporter.user).count())
        notification = Notification.objects.filter(user=supporter.user).last()
        self.assertEqual(notification.user, supporter.user)

    def test_decorate_add_review(self):
        self.assertEqual(0, Action.objects.all().count())
        self.assertEqual(0, Notification.objects.all().count())

        athlete = AthleteFactory()
        ReviewFactory(athlete=athlete)

        self.assertEqual(1, Action.objects.all().count())
        self.assertEqual(1, Notification.objects.filter(user=athlete.user).count())
        notification = Notification.objects.filter(user=athlete.user).last()
        self.assertEqual(notification.user, athlete.user)

    def test_decorate_add_purchase(self):
        self.assertEqual(0, Action.objects.all().count())
        self.assertEqual(0, Notification.objects.all().count())

        athlete = AthleteFactory()
        supporter = SupporterFactory()
        token = TokenFactory(athlete=athlete, amount=1000, price=1000)
        PurchaseFactory(token=token, supporter=supporter, amount=10)

        self.assertEqual(1, Action.objects.all().count())
        self.assertEqual(1, Notification.objects.filter(user=athlete.user).count())
        notification = Notification.objects.filter(user=athlete.user).last()
        self.assertEqual(notification.user, athlete.user)
