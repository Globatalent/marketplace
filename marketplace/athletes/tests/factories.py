import datetime

import factory

from marketplace.users.tests.factories import UserFactory
from marketplace.athletes.constants import APPROVED


class AthleteFactory(factory.django.DjangoModelFactory):

    date_of_birth = datetime.date.today()
    user = factory.SubFactory(UserFactory)
    state = APPROVED

    class Meta:
        model = "athletes.Athlete"
