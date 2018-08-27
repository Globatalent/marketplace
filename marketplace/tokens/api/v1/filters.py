import django_filters
from django.utils.translation import ugettext_lazy as _

from marketplace.tokens.models import Token


class TokenFilter(django_filters.rest_framework.FilterSet):

    athlete_id = django_filters.NumberFilter(
        name="athlete__id",
        help_text=_("Filter using the athlete internal ID.")
    )

    class Meta:
        model = Token
        fields = ['athlete_id']
