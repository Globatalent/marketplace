import hashlib
import random
import time

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from marketplace.core.tasks import send_mail_task
from marketplace.users.emails import RestorePasswordEmail, VerificationEmail


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
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

    def save(self, *args, **kwargs):
        is_insert = self.pk is None
        # Checks change of email
        if not is_insert:
            previous_user = User.objects.get(pk=self.pk)
            if previous_user.email != self.email:
                self.is_email_verified = False
                self.verification_code = None
        # Creates verification code if it doesn't exists
        if not self.is_email_verified and (self.verification_code is None or self.verification_code.strip() == ""):
            self.verification_code = self.generate_random_code()
        result = super().save(*args, **kwargs)
        # For every inserts, sends a verification email (excepts superusers)
        if not self.is_email_verified and not self.is_superuser:
            self.send_verification()
        return result
