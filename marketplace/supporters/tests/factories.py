import factory

from marketplace.users.tests.factories import UserFactory


class SupporterFactory(factory.django.DjangoModelFactory):

    user = factory.SubFactory(UserFactory)

    class Meta:
        model = "supporters.Supporter"
