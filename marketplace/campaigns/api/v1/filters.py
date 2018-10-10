import django_filters
from django.utils.translation import ugettext_lazy as _

from marketplace.campaigns.models import Campaign


class CampaignFilter(django_filters.rest_framework.FilterSet):

    is_draft = django_filters.BooleanFilter(
        field_name='is_draft',
        help_text=_("Filter draft campaigns.")
    )
    kind = django_filters.CharFilter(
        field_name='kind',
        help_text=_("Filter campaigns by kind.")
    )
    user = django_filters.NumberFilter(
        field_name='user__id',
        help_text=_("Filter campaigns by given user.")
    )
    followed_by = django_filters.NumberFilter(
        field_name="followers__id",
        help_text=_("Filter the athletes followed by the user given by ID.")
    )

    class Meta:
        model = Campaign
        fields = ["is_draft", "kind", "user", "followed_by"]
