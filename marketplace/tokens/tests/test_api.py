from rest_framework import status
from rest_framework.test import APITestCase

from marketplace.athletes.tests.factories import AthleteFactory
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
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['count'], len(tokens))

    def test_list_tokens_by_athlete(self):
        tokens = TokenFactory.create_batch(size=5)
        self.client.force_authenticate(self.user)
        response = self.client.get(
            "/api/v1/tokens/?athlete_id={}".format(tokens[0].athlete.id),
            format="json",
        )
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['count'], 1)

    def test_create_token(self):
        athlete = AthleteFactory()
        self.client.force_authenticate(athlete.user)
        data = {
            "amount": 1000,
            "price": 100,
        }
        response = self.client.post(
            "/api/v1/tokens/",
            data=data,
            format="json",
        )
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
