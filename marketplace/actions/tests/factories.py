import factory
from django.contrib.contenttypes.models import ContentType

from marketplace.campaigns.tests.factories import CampaignFactory
from marketplace.users.tests.factories import UserFactory


class ActionFactory(factory.django.DjangoModelFactory):

    actor_object_id = factory.SelfAttribute("actor.id")
    actor_content_type = factory.LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.actor)
    )

    class Meta:
        exclude = ["actor"]
        abstract = True


class ActionCampaignFactory(ActionFactory):

    actor = factory.SubFactory(CampaignFactory)

    class Meta:
        model = "actions.Action"


class NotificationFactory(factory.django.DjangoModelFactory):

    user = factory.SubFactory(UserFactory)
    action = factory.SubFactory(ActionCampaignFactory)

    class Meta:
        model = "actions.Notification"
