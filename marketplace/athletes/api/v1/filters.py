import django_filters
from django.utils.translation import ugettext_lazy as _

from marketplace.athletes.models import Athlete


class AthleteFilter(django_filters.rest_framework.FilterSet):

    followed_by = django_filters.NumberFilter(
        name="supporters__user__id",
        help_text=_("Filter the athletes followed by the user given by ID.")
    )

    class Meta:
        model = Athlete
        fields = ['followed_by']
