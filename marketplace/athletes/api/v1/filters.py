import django_filters
from django.utils.translation import ugettext_lazy as _

from marketplace.athletes.models import Athlete, Review


class AthleteFilter(django_filters.rest_framework.FilterSet):

    followed_by = django_filters.NumberFilter(
        name="supporters__user__id",
        help_text=_("Filter the athletes followed by the user given by ID.")
    )
    state = django_filters.CharFilter(
        name="state",
        help_text=_("Filter the athletes by the state.")
    )

    class Meta:
        model = Athlete
        fields = ['followed_by', 'state']


class ReviewFilter(django_filters.rest_framework.FilterSet):

    state = django_filters.CharFilter(
        name="state",
        help_text=_("Filter the reviews by the state.")
    )

    class Meta:
        model = Review
        fields = ['state']
