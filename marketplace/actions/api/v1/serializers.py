from generic_relations.relations import GenericRelatedField
from rest_framework import serializers

from marketplace.actions.models import Notification, Action
from marketplace.athletes.api.v1.serializers import AthleteSerializer, PictureSerializer, ReviewSerializer
from marketplace.athletes.models import Athlete, Picture, Review
from marketplace.supporters.api.v1.serializers import SupporterSerializer
from marketplace.supporters.models import Supporter
from marketplace.users.api.v1.serializers import UserSerializer
from marketplace.users.models import User


class ActionSerializer(serializers.ModelSerializer):

    text = serializers.CharField(read_only=True)
    actor = GenericRelatedField({
        Supporter: SupporterSerializer(),
        Athlete: AthleteSerializer(),
        User: UserSerializer(),
    })
    trigger = GenericRelatedField({
        Supporter: SupporterSerializer(),
        Athlete: AthleteSerializer(),
        User: UserSerializer(),
        Picture: PictureSerializer(),
        Review: ReviewSerializer(),
    })
    target = GenericRelatedField({
        Supporter: SupporterSerializer(),
        Athlete: AthleteSerializer(),
        User: UserSerializer(),
        Picture: PictureSerializer(),
        Review: ReviewSerializer(),
    })

    class Meta:
        model = Action
        fields = [
            'id',
            'actor',
            'verb',
            'target',
            'trigger',
            'text',
            'created',
        ]


class NotificationSerializer(serializers.ModelSerializer):

    action = ActionSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = [
            'id',
            'read',
            'read_at',
            'action',
            'created',
        ]

