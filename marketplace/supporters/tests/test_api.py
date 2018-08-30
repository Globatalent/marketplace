from rest_framework import status
from rest_framework.test import APITestCase

from marketplace.athletes.tests.factories import AthleteFactory
from marketplace.supporters.models import Supporter
from marketplace.users.models import User
from marketplace.users.tests.factories import UserFactory
from marketplace.supporters.constants import UP
from marketplace.supporters.tests.factories import SupporterFactory
from supporters.tests.factories import AlertFactory


class SupportersAPITests(APITestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_register_supporter(self):
        users = User.objects.all().count()
        supporters = Supporter.objects.all().count()
        data = {
            "email": "foo@example.com",
            "password": "pass1234",
            "repeat_password": "pass1234",
        }
        response = self.client.post(
            "/api/v1/register/supporter/",
            format="json",
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(supporters + 1, Supporter.objects.all().count())
        self.assertEqual(users + 1, User.objects.all().count())
        data = response.json()
        self.assertIn("token", data)
        self.assertIsNotNone(data["token"])

    def test_create_alert(self):
        athlete = AthleteFactory()
        supporter = SupporterFactory()
        self.client.force_authenticate(supporter.user)
        data = {
            "rule": UP,
            "amount": 100,
            "athlete": athlete.pk,
        }
        response = self.client.post(
            "/api/v1/alerts/",
            format="json",
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_alerts(self):
        supporter = SupporterFactory()
        alerts = AlertFactory.create_batch(supporter=supporter, size=5)
        self.client.force_authenticate(supporter.user)
        response = self.client.get(
            "/api/v1/alerts/",
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(alerts), data['count'])