import factory
from factory.fuzzy import FuzzyDecimal, FuzzyInteger


class TokenFactory(factory.django.DjangoModelFactory):

    amount = FuzzyInteger(1, 1000)
    price = FuzzyDecimal(1.0, 1000.0)

    class Meta:
        model = "tokens.Token"
