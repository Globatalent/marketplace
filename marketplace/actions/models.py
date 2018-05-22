from django.db import models
from django.utils.translation import ugettext_lazy as _

from marketplace.users.models import User


class ActionType(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('action type')
        verbose_name_plural = _('action types')


class Action(models.Model):
    text = models.TextField(verbose_name=_('text'))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_('date'))
    link = models.URLField(verbose_name=_('link'))
    type = models.ForeignKey(ActionType, verbose_name=_('type'),
                             related_name='actions', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _('action')
        verbose_name_plural = _('actions')


class Notification(models.Model):
    read = models.BooleanField(default=False)
    user = models.ForeignKey(User, verbose_name=_('user'),
                             related_name='notifications', on_delete=models.CASCADE)
    action = models.ForeignKey(Action, verbose_name=_('action'),
                               related_name='notifications', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _('notification')
        verbose_name_plural = _('notifications')
