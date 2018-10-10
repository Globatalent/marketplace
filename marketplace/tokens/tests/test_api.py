from rest_framework import status
from rest_framework.test import APITestCase

from marketplace.campaigns.tests.factories import CampaignFactory
from marketplace.tokens.tests.factories import TokenFactory
from marketplace.users.tests.factories import UserFactory


class TokensAPITests(APITestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_list_tokens(self):
        tokens = TokenFactory.create_batch(size=5)
        self.client.force_authenticate(self.user)
        response = self.client.get(
            "/api/v1/tokens/",
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['count'], len(tokens))

    def test_list_tokens_by_campaign(self):
        campaigns = CampaignFactory.create_batch(is_draft=False, funds=1000, size=5)
        self.client.force_authenticate(self.user)
        response = self.client.get(
            "/api/v1/tokens/?campaign_id={}".format(campaigns[0].id),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['count'], 1)
