from rest_framework import serializers

from marketplace.alerts.models import Alert


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ('id', 'rule', 'amount', 'campaign')
        extra_kwargs = {
            "supporter": {'read_only': True}
        }

