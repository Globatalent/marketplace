from generic_relations.relations import GenericRelatedField
from rest_framework import serializers

from marketplace.actions.models import Notification, Action
from marketplace.campaigns.api.v1.serializers import CampaignSerializer
from marketplace.campaigns.models import Campaign
from marketplace.purchases.api.v1.serializers import PurchaseSerializer
from marketplace.purchases.models import Purchase
from marketplace.users.api.v1.serializers import UserSerializer
from marketplace.users.models import User


class ActionSerializer(serializers.ModelSerializer):

    text = serializers.CharField(read_only=True)
    actor = GenericRelatedField({
        User: UserSerializer(),
        Campaign: CampaignSerializer(),
    })
    trigger = GenericRelatedField({
        User: UserSerializer(),
        Purchase: PurchaseSerializer(),
        Campaign: CampaignSerializer(),
    })
    target = GenericRelatedField({
        User: UserSerializer(),
        Purchase: PurchaseSerializer(),
        Campaign: CampaignSerializer(),
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

