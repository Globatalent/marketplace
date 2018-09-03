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


class PictureFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = "athletes.Picture"


class ReviewFactory(factory.django.DjangoModelFactory):

    reviewer = factory.SubFactory(UserFactory)
    athlete = factory.SubFactory(AthleteFactory)

    class Meta:
        model = "athletes.Review"

