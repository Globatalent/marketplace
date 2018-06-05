from django.db import models
from django.utils.translation import ugettext_lazy as _

from marketplace.athletes.models import Athlete
from marketplace.users.models import User


class Supporter(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('user')
    )
    # TODO: Change 'APPROVED' to Athlete.APPROVED
    following = models.ManyToManyField(Athlete, blank=True, related_name='suppoters',
                                       verbose_name=_('following'))

    def __str__(self):
        return f'{str(self.id)} - {self.user.email}'

    class Meta:
        verbose_name = _('supporter')
        verbose_name_plural = _('supporters')


class Alert(models.Model):
    UP = 'UP'
    DOWN = 'DOWN'
    RULE_CHOICES = (
        (UP, _('Go up')),
        (DOWN, _('Go down')),
    )
    rule = models.CharField(choices=RULE_CHOICES, default=UP, max_length=10, verbose_name=_('rule'))
    amount = models.FloatField(verbose_name=_('amount'))
    supporter = models.ForeignKey(Supporter, verbose_name=_('supporter'),
                                  related_name='alerts', on_delete=models.CASCADE)
    athlete = models.ForeignKey(Athlete, verbose_name=_('athlete'),
                                related_name='alerts', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _('alert')
        verbose_name_plural = _('alerts')
