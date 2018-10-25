import hashlib
import random
import time

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from marketplace.actions.constants import FOLLOWS, UNFOLLOWS
from marketplace.actions.decorators import dispatch_action
from marketplace.core.tasks import send_mail_task
from marketplace.users.emails import RestorePasswordEmail, VerificationEmail, ChangedPasswordEmail, VerifiedEmail
from marketplace.users.helpers import is_following
from marketplace.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=100, verbose_name=_('first name'), default="")
    last_name = models.CharField(max_length=100, verbose_name=_('last name'), default="")
    birth_date = models.DateField(verbose_name=_('birth date'), null=True)

    email = models.EmailField(verbose_name=_('email address'), unique=True, blank=True,
                              error_messages={'unique': _('There is another user with this email')})
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(verbose_name=_('date joined'), default=timezone.now)

    following = models.ManyToManyField(
        "campaigns.Campaign",
        blank=True,
        related_name='followers',
        verbose_name=_('following'),
        limit_choices_to={'is_draft': False}
    )

    # Restore password
    restore_password_code = models.CharField(max_length=256, unique=True, null=True, blank=True)
    restore_password_code_requested_at = models.DateTimeField(null=True, blank=True)

    # Email verification
    is_email_verified = models.BooleanField(
        _("verified"),
        default=False,
        help_text=_("Designates if the user has the email verified")
    )
    verification_code = models.CharField(max_length=256, unique=True, null=True, blank=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ["-date_joined"]

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail_task.delay(subject, message, from_email, [self.email], **kwargs)

    def generate_random_code(self):
        """Generates a restore password code."""
        return hashlib.sha256(
            ("{}-{}-{}".format(self.email, time.time(), random.randint(0, 10))).encode('utf-8')
        ).hexdigest()

    def send_restore_code(self):
        """Sends an email with the link to restore the password."""
        self.restore_password_code = self.generate_random_code()
        self.restore_password_code_requested_at = timezone.now()
        self.save()
        email = RestorePasswordEmail(to=self.email, context={"user": self})
        email.send()

    def send_verification(self):
        """Send the validation email, to validate the user's email."""
        assert self.pk is not None
        assert not self.is_email_verified
        assert self.verification_code is not None

        email = VerificationEmail(to=self.email, context={"user": self})
        email.send()

    def verify(self):
        """Verifies this email user."""
        self.is_email_verified = True
        self.verification_code = None
        self.save()
        email = VerifiedEmail(to=self.email, context={"user": self})
        email.send()

    def follow(self, campaign):
        """The given campaign is followed by the current user and returns True.
        If the user is following the campaign, then the user stop
        following the campaign, and return False.
        """
        if is_following(self, campaign):
            return self._unfollow(campaign)
        return self._follow(campaign)

    @dispatch_action(FOLLOWS, method=True)
    def _follow(self, campaign):
        self.following.add(campaign)
        return True

    @dispatch_action(UNFOLLOWS, method=True)
    def _unfollow(self, campaign):
        self.following.remove(campaign)
        return False

    def send_changed_password(self):
        """Sends the email for password change."""
        email = ChangedPasswordEmail(to=self.email, context={"user": self})
        email.send()

    def save(self, *args, **kwargs):
        is_insert = self.pk is None
        # Checks change of email
        if not is_insert:
            previous_user = User.objects.get(pk=self.pk)
            if previous_user.email != self.email:
                self.is_email_verified = False
                self.verification_code = None
            if previous_user.password != self.password:
                self.send_changed_password()
        # Creates verification code if it doesn't exists
        if not self.is_email_verified and (self.verification_code is None or self.verification_code.strip() == ""):
            self.verification_code = self.generate_random_code()
        result = super().save(*args, **kwargs)
        # For every inserts, sends a verification email (excepts superusers)
        if not self.is_email_verified and not self.is_superuser:
            self.send_verification()
        return result
