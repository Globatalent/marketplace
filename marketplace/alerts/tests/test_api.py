from rest_framework import status
from rest_framework.test import APITestCase

from marketplace.alerts.constants import UP
from marketplace.alerts.tests.factories import AlertFactory
from marketplace.campaigns.tests.factories import CampaignFactory
from marketplace.users.tests.factories import UserFactory


class AlertsAPITests(APITestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_create_alert(self):
        campaign = CampaignFactory()

        self.client.force_authenticate(self.user)
        data = {"rule": UP, "amount": 100, "campaign": campaign.pk}
        response = self.client.post("/api/v1/alerts/", format="json", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_alerts(self):
        alerts = AlertFactory.create_batch(user=self.user, size=5)
        self.client.force_authenticate(self.user)
        response = self.client.get("/api/v1/alerts/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(alerts), data["count"])
