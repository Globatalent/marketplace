import factory
from factory.fuzzy import FuzzyDecimal, FuzzyInteger

from marketplace.athletes.tests.factories import AthleteFactory


class TokenFactory(factory.django.DjangoModelFactory):

    athlete = factory.SubFactory(AthleteFactory)
    amount = FuzzyInteger(1, 1000)
    price = FuzzyDecimal(1.0, 1000.0)

    class Meta:
        model = "tokens.Token"
