from rest_framework import serializers

from marketplace.tokens.models import Token


class TokenSerializer(serializers.ModelSerializer):

    unit_price = serializers.FloatField(read_only=True)
    remaining = serializers.IntegerField(read_only=True)
    progression = serializers.FloatField(read_only=True)

    class Meta:
        model = Token
        fields = [
            "id",
            "campaign",
            "name",
            "code",
            "amount",
            "price",
            "unit_price",
            "remaining",
            "progression",
            "currency",
        ]
        extra_kwargs = {"campaign": {"read_only": True}}
