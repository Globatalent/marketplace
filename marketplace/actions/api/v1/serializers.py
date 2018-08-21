from rest_framework import serializers

from marketplace.actions.models import Notification, Action


class ActionSerializer(serializers.ModelSerializer):

    text = serializers.CharField(read_only=True)

    class Meta:
        model = Action
        fields = [
            'id',
            'actor_content_type',
            'actor_object_id',
            'verb',
            'target_content_type',
            'target_object_id',
            'trigger_content_type',
            'trigger_object_id',
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

