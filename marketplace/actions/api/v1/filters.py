import django_filters
from django.utils.translation import ugettext_lazy as _

from marketplace.actions.models import Notification


class NotificationFilter(django_filters.rest_framework.FilterSet):

    read = django_filters.BooleanFilter(
        field_name="read",
        help_text=_("Filter by read or not notifications.")
    )

    class Meta:
        model = Notification
        fields = ['read']
