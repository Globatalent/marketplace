import factory
from factory.fuzzy import FuzzyDecimal

from marketplace.athletes.tests.factories import AthleteFactory
from marketplace.users.tests.factories import UserFactory


class SupporterFactory(factory.django.DjangoModelFactory):

    user = factory.SubFactory(UserFactory)

    class Meta:
        model = "supporters.Supporter"


class AlertFactory(factory.django.DjangoModelFactory):
    amount = FuzzyDecimal(0.0)
    supporter = factory.SubFactory(SupporterFactory)
    athlete = factory.SubFactory(AthleteFactory)

    class Meta:
        model = "supporters.Alert"
