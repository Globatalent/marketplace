from rest_framework import serializers

from marketplace.purchases.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = [
            "id",
            "token",
            "amount",
            "status",
            "total",
        ]
        extra_kwargs = {
            "total": {"read_only": True},
            "status": {"read_only": True}
        }
