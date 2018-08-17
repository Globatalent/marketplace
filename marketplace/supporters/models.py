from django.db import models
from django.utils.translation import ugettext_lazy as _

from marketplace.athletes.constants import APPROVED
from marketplace.users.models import User
from marketplace.supporters.constants import RULE_CHOICES, UP


class Supporter(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('user')
    )
    following = models.ManyToManyField(
        "athletes.Athlete",
        blank=True,
        related_name='supporters',
        verbose_name=_('following'),
        limit_choices_to={'state': APPROVED}
    )

    class Meta:
        verbose_name = _('supporter')
        verbose_name_plural = _('supporters')

    def __str__(self):
        return f'{str(self.id)} - {self.user.email}'

    def follow(self, athlete):
        """The given athlete is followed by the current supporter and returns True.
        If the supporter is following the athlete, then the supporter stop
        following the athlete, and return False.
        """
        if self.following.filter(pk=athlete.pk).exists():
            self.following.remove(athlete)
            return False
        self.following.add(athlete)
        return True


class Alert(models.Model):
    rule = models.CharField(choices=RULE_CHOICES, default=UP, max_length=10, verbose_name=_('rule'))
    amount = models.FloatField(verbose_name=_('amount'))
    supporter = models.ForeignKey(Supporter, verbose_name=_('supporter'),
                                  related_name='alerts', on_delete=models.CASCADE)
    athlete = models.ForeignKey("athletes.Athlete", verbose_name=_('athlete'),
                                related_name='alerts', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _('alert')
        verbose_name_plural = _('alerts')
