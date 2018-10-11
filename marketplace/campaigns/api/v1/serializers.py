from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from marketplace.campaigns.models import Campaign, Sport, Picture, Link, Revenue, Income, Recommendation
from marketplace.tokens.api.v1.serializers import TokenSerializer
from marketplace.users.helpers import is_following


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = [
            "id",
            "name",
        ]


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = [
            "campaign",
            "image",
        ]


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = [
            "campaign",
            "network",
            "url",
        ]


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = [
            "campaign",
            "year",
            "currency",
            "amount",
        ]


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = [
            "campaign",
            "year",
            "currency",
            "amount",
        ]


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = [
            "campaign",
            "image",
        ]


class CampaignSerializer(serializers.ModelSerializer):

    links = LinkSerializer(
        many=True,
        required=False,
        read_only=True,
        help_text=_("List of links objects."),
    )
    revenues = RevenueSerializer(
        many=True,
        required=False,
        read_only=True,
        help_text=_("List of revenues objects."),
    )
    incomes = IncomeSerializer(
        many=True,
        required=False,
        read_only=True,
        help_text=_("List of incomes objects."),
    )
    recommendations = RecommendationSerializer(
        many=True,
        required=False,
        read_only=True,
        help_text=_("List of recommendations objects."),
    )
    token = TokenSerializer(read_only=True)
    following = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Campaign
        fields = [
            "id",
            "is_draft",
            "token",
            "title",
            "description",
            "image",
            "gender",
            "sport",
            "tags",
            "gender",
            "height",
            "weight",
            "club",
            "coach",
            "pitch_url",
            "pitch_image",
            "ranking",
            "biography",
            "achievements",
            "expected",
            "funds",
            "use",
            "give_back",
            "examples",
            "links",
            "revenues",
            "incomes",
            "recommendations",
            'following',
            "created",
        ]
        extra_kwargs = {
            "created": {"read_only": True},
            "token": {"read_only": True},
        }

    def get_following(self, obj):
        """Gets if the user who makes the request is following the campaign."""
        if 'request' in self.context:
            user = self.context['request'].user
            return is_following(user, obj)
        return False


class ReadCampaignSerializer(CampaignSerializer):
    sport = SportSerializer(read_only=True)
