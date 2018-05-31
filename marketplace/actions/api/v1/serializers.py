from rest_framework import serializers

from marketplace.actions.models import Notification, Action, ActionType
from marketplace.users.api.v1.serializers import UserSerializer


class ActionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionType
        fields = ('id', 'name')


class ActionSerializer(serializers.ModelSerializer):
    type = ActionTypeSerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Action
        fields = ('id', 'text', 'date', 'link', 'type', 'user')


class NotificationSerializer(serializers.ModelSerializer):
    actions = ActionSerializer(many=True, read_only=True)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Notification
        fields = ('id', 'read', 'actions', 'user')

