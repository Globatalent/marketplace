from rest_framework import status
from rest_framework.test import APITestCase

from marketplace.actions.tests.factories import NotificationFactory
from marketplace.users.tests.factories import UserFactory


class ActionsAPITests(APITestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_list_notifications(self):
        NotificationFactory.create_batch(size=5)
        notifications = NotificationFactory.create_batch(user=self.user, size=5)
        self.client.force_authenticate(self.user)
        response = self.client.get(
            "/api/v1/notifications/",
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(notifications), data["count"])
