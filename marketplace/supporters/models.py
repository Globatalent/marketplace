from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from marketplace.actions.decorators import dispatch_action
from marketplace.athletes.constants import APPROVED
from marketplace.supporters.constants import RULE_CHOICES, UP
from marketplace.supporters.helpers import is_following
from marketplace.users.models import User


class Supporter(models.Model):
    """Supporter profile of the user."""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('user')
    )
    first_name = models.CharField(max_length=100, verbose_name=_('first name'), default="")
    last_name = models.CharField(max_length=100, verbose_name=_('last name'), default="")
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
        if self.first_name or self.last_name:
            return " ".join([self.first_name, self.last_name])
        return str(self.user)


    def follow(self, athlete):
        """The given athlete is followed by the current supporter and returns True.
        If the supporter is following the athlete, then the supporter stop
        following the athlete, and return False.
        """
        if is_following(self, athlete):
            return self._unfollow(athlete)
        return self._follow(athlete)


    @dispatch_action("follows", method=True)
    def _follow(self, athlete):
        self.following.add(athlete)
        return True

    @dispatch_action("unfollow", method=True)
    def _unfollow(self, athlete):
        self.following.remove(athlete)
        return False


class Alert(TimeStampedModel):
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
        ordering = ('-created', )
