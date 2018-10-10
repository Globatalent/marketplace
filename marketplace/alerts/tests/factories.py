import factory
from factory.fuzzy import FuzzyDecimal

from marketplace.campaigns.tests.factories import CampaignFactory
from marketplace.users.tests.factories import UserFactory


class AlertFactory(factory.django.DjangoModelFactory):
    amount = FuzzyDecimal(0.0)
    user = factory.SubFactory(UserFactory)
    campaign = factory.SubFactory(CampaignFactory)

    class Meta:
        model = "alerts.Alert"
