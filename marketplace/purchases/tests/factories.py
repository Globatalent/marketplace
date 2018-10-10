import factory

from marketplace.tokens.tests.factories import TokenFactory
from marketplace.users.tests.factories import UserFactory


class PurchaseFactory(factory.django.DjangoModelFactory):

    user = factory.SubFactory(UserFactory)
    token = factory.SubFactory(TokenFactory)

    class Meta:
        model = "purchases.Purchase"
