import factory

from marketplace.tokens.tests.factories import TokenFactory
from marketplace.users.tests.factories import UserFactory


class CampaignFactory(factory.django.DjangoModelFactory):

    user = factory.SubFactory(UserFactory)
    title = factory.Faker("sentence", nb_words=4)
    description = factory.Faker("sentence", nb_words=4)
    image = factory.django.ImageField(color="red")
    token = factory.SubFactory(TokenFactory)

    class Meta:
        model = "campaigns.Campaign"
