from django.db import models
from django.utils.translation import ugettext_lazy as _

from marketplace.users.models import User


class Athlete(models.Model):
    UNINITIALIZED = 'NONE'
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    SEX_CHOICES = (
        (UNINITIALIZED, _('Uninitialized')),
        (MALE, _('Male')),
        (FEMALE, _('Female'))
    )
    first_name = models.CharField(max_length=100, verbose_name=_('first name'))
    last_name = models.CharField(max_length=100, verbose_name=_('last name'))
    country = models.CharField(max_length=100, verbose_name=_('country'))
    state = models.CharField(max_length=100, verbose_name=_('state'))
    sex = models.CharField(choices=SEX_CHOICES, default=UNINITIALIZED, max_length=20, verbose_name=_('sex'))
    date_of_birthday = models.DateTimeField(verbose_name=_('date of birthday'))
    sport = models.CharField(max_length=200, verbose_name=_('sport'))
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('user')
    )

