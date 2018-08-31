from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
from model_utils.models import TimeStampedModel

from marketplace.actions.constants import ADD_PICTURE, ADD_REVIEW
from marketplace.actions.decorators import dispatch_action
from marketplace.athletes.constants import SEX_CHOICES, STATE_CHOICES, PENDING_REVIEW
from marketplace.core.files import UploadToDir
from marketplace.users.models import User


class Athlete(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_('first name'))
    last_name = models.CharField(max_length=100, verbose_name=_('last name'))
    country = models.CharField(max_length=100, verbose_name=_('country'))
    sex = models.CharField(choices=SEX_CHOICES, null=True, blank=True, max_length=20, verbose_name=_('sex'))
    date_of_birth = models.DateField(verbose_name=_('date of birth'))
    sport = models.CharField(max_length=200, verbose_name=_('sport'))
    state = models.CharField(choices=STATE_CHOICES, default=PENDING_REVIEW, max_length=20, verbose_name=_('state'))
    biography = models.TextField(null=True, blank=True, verbose_name=_('biography'))
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('user')
    )

    class Meta:
        verbose_name = _('athlete')
        verbose_name_plural = _('athletes')
        ordering = ("user__date_joined", )

    def __str__(self):
        return " ".join([self.first_name, self.last_name])

    @property
    def token(self):
        """Gets the last token created by the athlete."""
        return self.tokens.last()


class Picture(models.Model):
    image = ThumbnailerImageField(
        max_length=250,
        upload_to=UploadToDir('athletes', populate_from='athlete_id'),
        verbose_name=_('image'),
    )
    athlete = models.ForeignKey(Athlete, verbose_name=_('athlete'),
                                related_name='pictures', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _('picture')
        verbose_name_plural = _('pictures')

    @dispatch_action(ADD_PICTURE, method=True)
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class Link(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('name'))
    url = models.URLField(null=True, blank=True, verbose_name=_('url'))
    athlete = models.ForeignKey(Athlete, verbose_name=_('athlete'),
                                related_name='links', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('link')
        verbose_name_plural = _('links')


class Review(TimeStampedModel):
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'
    REVIEWING = 'REVIEWING'
    PENDING_REVIEW = 'PENDING_REVIEW'
    STATE_CHOICES = (
        (APPROVED, _('Approved')),
        (REJECTED, _('Rejected')),
        (REVIEWING, _('Reviewing')),
        (PENDING_REVIEW, _('Pending Review')),
    )
    text = models.TextField(null=True, blank=True, verbose_name=_('text'))
    state = models.CharField(choices=STATE_CHOICES, default=PENDING_REVIEW, max_length=20, verbose_name=_('state'))
    reviewer = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True},
        verbose_name=_('user')
    )
    athlete = models.ForeignKey(Athlete, verbose_name=_('review'),
                                related_name='reviews', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('review')
        verbose_name_plural = _('reviews')
        ordering = ("created", )

    def __str__(self):
        return f'{str(self.athlete)} - {self.state}'

    @dispatch_action(ADD_REVIEW, method=True)
    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)
        # Update athlete state
        last_review = self.athlete.reviews.last()
        self.athlete.state = last_review.state
        self.athlete.save()
        return result
