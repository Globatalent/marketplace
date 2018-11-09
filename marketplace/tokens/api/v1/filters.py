import django_filters
from django.utils.translation import ugettext_lazy as _

from marketplace.tokens.models import Token


class TokenFilter(django_filters.rest_framework.FilterSet):

    campaign_id = django_filters.NumberFilter(
        field_name="campaign__id", help_text=_("Filter using the campaign internal ID.")
    )

    class Meta:
        model = Token
        fields = ["campaign_id"]
