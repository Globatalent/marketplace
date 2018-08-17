import datetime

import factory

from marketplace.users.tests.factories import UserFactory


class AthleteFactory(factory.django.DjangoModelFactory):

    date_of_birth = datetime.date.today()
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = "athletes.Athlete"
