from test_plus.test import TestCase

from marketplace.actions.models import Action, Notification
from marketplace.athletes.tests.factories import AthleteFactory
from marketplace.supporters.tests.factories import SupporterFactory
from marketplace.users.tests.factories import UserFactory


class ActionsDecoratorsTests(TestCase):
    user_factory = UserFactory

    def setUp(self):
        self.user = self.make_user()

    def test_decorate_method(self):
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
