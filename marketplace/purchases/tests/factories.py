import factory

from marketplace.supporters.tests.factories import SupporterFactory
from marketplace.tokens.tests.factories import TokenFactory


class PurchaseFactory(factory.django.DjangoModelFactory):

    supporter = factory.SubFactory(SupporterFactory)
    token = factory.SubFactory(TokenFactory)

    class Meta:
        model = "purchases.Purchase"
