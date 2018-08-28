from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import password_validation
from django.utils.translation import ugettext_lazy as _

from marketplace.tokens.models import Token, Purchase


class TokenSerializer(serializers.ModelSerializer):

    unit_price = serializers.IntegerField(read_only=True)
    remaining = serializers.IntegerField(read_only=True)
    progression = serializers.FloatField(read_only=True)

    class Meta:
        model = Token
        fields = [
            "id",
            "athlete",
            "amount",
            "price",
            "unit_price",
            "remaining",
            "progression",
        ]
        extra_kwargs = {
            "athlete": {"read_only": True}
        }


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
