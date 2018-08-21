import factory
from django.contrib.contenttypes.models import ContentType

from marketplace.athletes.tests.factories import AthleteFactory
from marketplace.users.tests.factories import UserFactory


class ActionFactory(factory.django.DjangoModelFactory):

    actor_object_id = factory.SelfAttribute('actor.id')
    actor_content_type = factory.LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.actor))

    class Meta:
        exclude = ['actor']
        abstract = True


class ActionAthleteFactory(ActionFactory):

    actor = factory.SubFactory(AthleteFactory)

    class Meta:
        model = "actions.Action"


class NotificationFactory(factory.django.DjangoModelFactory):

    user = factory.SubFactory(UserFactory)
    action = factory.SubFactory(ActionAthleteFactory)

    class Meta:
        model = "actions.Notification"
