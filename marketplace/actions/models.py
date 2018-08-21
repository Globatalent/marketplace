from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from marketplace.athletes.models import Athlete
from marketplace.supporters.models import Supporter
from marketplace.users.models import User


class Action(TimeStampedModel):
    """A 'action' is generated when an 'actor' performs 'verb', involving 'action',
    in the 'target'.

     It could be:
        <actor> <verb>
        <actor> <verb> <target>
        <actor> <verb> <trigger> <target>

    Reference: http://activitystrea.ms/specs/atom/1.0/
    """

    actor_content_type = models.ForeignKey(
        ContentType,
        related_name='actor_actions',
        null=True,
        on_delete=models.CASCADE,
    )
    actor_object_id = models.PositiveIntegerField(null=True)
    actor = GenericForeignKey('actor_content_type', 'actor_object_id')

    verb = models.CharField(max_length=255, null=True)

    trigger_content_type = models.ForeignKey(
        ContentType,
        related_name='trigger_actions',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    trigger_object_id = models.PositiveIntegerField(blank=True, null=True)
    trigger = GenericForeignKey('trigger_content_type', 'trigger_object_id')

    target_content_type = models.ForeignKey(
        ContentType,
        related_name='target_actions',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    target_object_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')

    sent = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('action')
        verbose_name_plural = _('actions')

    def __str__(self):
        return self.text()

    def text(self):
        text = "{} {}".format(str(self.actor), self.verb)
        if self.trigger:
            text = "{} {}".format(text, str(self.trigger))
        if self.target:
            text = "{} {}".format(text, str(self.target))
        return text

    def audience(self):
        """Gets the audience of this action."""
        # If the actor is an athlete
        if self.actor_content_type == ContentType.objects.get_for_model(Athlete):
            supporters = self.actor.supporters.all()
            return User.objects.filter(pk__in=supporters.values_list('user__pk', flat=True))

        # If the actor is a support and the trigger is and athlete
        if self.actor_content_type == ContentType.objects.get_for_model(Supporter) and \
           self.trigger_content_type == ContentType.objects.get_for_model(Athlete):
            return User.objects.filter(pk=self.trigger.user.pk)

        return User.objects.none()

    def send(self):
        """Creates the notifications associated to this action, ."""
        for user in self.audience():
            notification = Notification(action=self, user=user)
            notification.save()
        self.sent = True
        self.save()

    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)
        if not self.sent:
            self.send()
        return result


class Notification(TimeStampedModel):
    """A 'notification' is a specific action that should be notified to an user."""
    action = models.ForeignKey(
        "actions.Action",
        on_delete=models.CASCADE,
        related_name='notifications',
        null=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        related_name='notifications',
        on_delete=models.CASCADE,
    )
    read = models.BooleanField(default=False)
    read_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = _('notification')
        verbose_name_plural = _('notifications')
        ordering = ('-created', )

    def __str__(self):
        return "{}: ".format(str(self.user), str(self.action))

    def save(self, *args, **kwargs):
        """Overwrite to handle 'read_at' field."""
        is_insert = self.pk is None
        if not is_insert:
            previous_notification = Notification.get(pk=self.pk)
            if not previous_notification.read and self.read:
                self.read_at = timezone.now()
        elif self.read:
            self.read_at = timezone.now()
        return super().save(*args, **kwargs)
