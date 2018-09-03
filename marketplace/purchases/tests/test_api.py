from rest_framework import status
from rest_framework.test import APITestCase

from marketplace.purchases.tests.factories import PurchaseFactory
from marketplace.supporters.tests.factories import SupporterFactory
from marketplace.tokens.tests.factories import TokenFactory
from marketplace.users.tests.factories import UserFactory


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
