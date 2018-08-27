from rest_framework import status
from rest_framework.test import APITestCase

from marketplace.users.tests.factories import UserFactory
from marketplace.athletes.tests.factories import AthleteFactory
from marketplace.supporters.tests.factories import SupporterFactory
from marketplace.tokens.tests.factories import TokenFactory, PurchaseFactory


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


class PurchasesAPITests(APITestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_purchase_token(self):
        supporter = SupporterFactory()
        token = TokenFactory(amount=1000, price=1)
        self.client.force_authenticate(supporter.user)
        data = {
            "token": token.pk,
            "amount": 10,
        }
        response = self.client.post(
            "/api/v1/purchases/",
            data=data,
            format="json",
        )
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_cant_purchase_token(self):
        supporter = SupporterFactory()
        token = TokenFactory(amount=1000, price=1)
        self.client.force_authenticate(token.athlete.user)
        data = {
            "token": token.pk,
            "amount": 10,
        }
        response = self.client.post(
            "/api/v1/purchases/",
            data=data,
            format="json",
        )
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    def test_list_purchases(self):
        tokens = TokenFactory.create_batch(amount=1000, size=5)
        supporter = SupporterFactory()
        purchases = PurchaseFactory.create_batch(
            token=tokens[0], supporter=supporter, amount=10, size=5
        )
        other_purchases = PurchaseFactory.create_batch(
            token=tokens[0], amount=10, size=6
        )
        self.client.force_authenticate(supporter.user)
        response = self.client.get(
            "/api/v1/purchases/",
            format="json"
        )
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['count'], len(purchases))
        self.client.force_authenticate(tokens[0].athlete.user)
        response = self.client.get(
            "/api/v1/purchases/",
            format="json"
        )
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['count'], len(purchases) + len(other_purchases))
