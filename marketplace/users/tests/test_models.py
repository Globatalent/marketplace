from test_plus.test import TestCase

from marketplace.users.tests.factories import UserFactory


class TestUser(TestCase):
    user_factory = UserFactory

    def setUp(self):
        self.user = self.make_user()

    def test__str__(self):
        self.assertEqual(
            self.user.__str__(),
            "testuser",  # This is the default username for self.make_user()
        )
