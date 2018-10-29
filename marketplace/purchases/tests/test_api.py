from rest_framework import status
from rest_framework.test import APITestCase

from marketplace.campaigns.tests.factories import CampaignFactory
from marketplace.purchases.tests.factories import PurchaseFactory
from marketplace.users.tests.factories import UserFactory


class PurchasesAPITests(APITestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_purchase_token(self):
        campaign = CampaignFactory(is_draft=False, funds=1000)
        self.client.force_authenticate(self.user)
        data = {"token": campaign.token.pk, "amount": 10}
        response = self.client.post("/api/v1/purchases/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_purchases(self):
        campaigns = CampaignFactory.create_batch(is_draft=False, funds=1000, size=5)
        purchases = PurchaseFactory.create_batch(
            token=campaigns[0].token, user=self.user, amount=10, size=5
        )
        PurchaseFactory.create_batch(token=campaigns[0].token, amount=10, size=6)
        self.client.force_authenticate(self.user)
        response = self.client.get("/api/v1/purchases/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["count"], len(purchases))
