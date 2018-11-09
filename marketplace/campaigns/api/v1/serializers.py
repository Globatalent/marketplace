from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from marketplace.campaigns.models import (
    Campaign,
    Sport,
    Picture,
    Link,
    Revenue,
    Income,
    Recommendation,
    Review,
)
from marketplace.tags.models import Tag
from marketplace.tokens.api.v1.serializers import TokenSerializer
from marketplace.users.helpers import is_following


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ["id", "name"]


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ["id", "campaign", "image"]


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["id", "campaign", "network", "url"]


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = ["id", "campaign", "year", "currency", "amount"]


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ["id", "campaign", "year", "currency", "amount"]


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ["id", "campaign", "file"]


class CampaignSerializer(serializers.ModelSerializer):

    links = LinkSerializer(
        many=True, required=False, read_only=True, help_text=_("List of links objects.")
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
    remaining = serializers.IntegerField(read_only=True)
    tags = serializers.ListField(
        required=False, child=serializers.CharField(), source="tag_names"
    )
    following = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Campaign
        fields = [
            "id",
            "is_draft",
            "kind",
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
            "following",
            "created",
            "history",
            "players",
            "started",
            "finished",
            "remaining",
            "rating",
        ]
        extra_kwargs = {
            "created": {"read_only": True},
            "token": {"read_only": True},
            "finished": {"read_only": True},
            "started": {"read_only": True},
        }

    def get_following(self, obj):
        """Gets if the user who makes the request is following the campaign."""
        if "request" in self.context:
            user = self.context["request"].user
            return is_following(user, obj)
        return False

    def validate_tags(self, value):
        """Gets or create tags."""
        tags = []
        for name in value:
            tag, created = Tag.objects.get_or_create(name=name, defaults={"name": name})
            tags.append(tag)
        return tags

    def create(self, validated_data):
        tags = (
            validated_data.pop("tag_names") if "tag_names" in validated_data else None
        )
        campaign = super().create(validated_data)
        if tags is not None:
            for tag in tags:
                campaign.tags.add(tag)
        return campaign

    def update(self, instance, validated_data):
        tags = (
            validated_data.pop("tag_names") if "tag_names" in validated_data else None
        )
        campaign = super().update(instance, validated_data)
        if tags is not None:
            campaign.tags.clear()
            for tag in tags:
                campaign.tags.add(tag)
        return campaign


class ReadCampaignSerializer(CampaignSerializer):
    sport = SportSerializer(read_only=True)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "text", "state", "campaign", "reviewer"]
        extra_kwargs = {"reviewer": {"read_only": True}}
