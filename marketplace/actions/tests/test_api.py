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

    def test_filter_notifications(self):
        NotificationFactory.create_batch(size=5)
        unread = NotificationFactory.create_batch(user=self.user, read=False, size=8)
        read = NotificationFactory.create_batch(user=self.user, read=True, size=4)
        self.client.force_authenticate(self.user)
        response = self.client.get(
            "/api/v1/notifications/count/?read=False",
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(unread), data["count"])
        response = self.client.get(
            "/api/v1/notifications/count/?read=True",
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(read), data["count"])

    def test_set_as_read(self):
        notification = NotificationFactory(user=self.user, read=False)
        self.client.force_authenticate(self.user)
        data = {
            "read": True
        }
        response = self.client.patch(
            "/api/v1/notifications/{}/".format(notification.pk),
            format="json",
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['read'])
        self.assertIsNotNone(data['read_at'])
