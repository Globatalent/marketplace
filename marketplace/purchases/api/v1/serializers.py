from rest_framework import serializers

from marketplace.purchases.models import Purchase
from marketplace.tokens.api.v1.serializers import TokenSerializer


class PurchaseSerializer(serializers.ModelSerializer):

    token = TokenSerializer()

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
