from django.db import models
from django.utils.translation import ugettext_lazy as _

from easy_thumbnails.fields import ThumbnailerImageField

from marketplace.core.files import UploadToDir
from marketplace.users.models import User


class Athlete(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    SEX_CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female'))
    )
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

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = _('athlete')
        verbose_name_plural = _('athletes')


class Picture(models.Model):
    image = ThumbnailerImageField(
        max_length=250,
        upload_to=UploadToDir('athletes', populate_from='athlete_id'),
        blank=False,
        verbose_name=_('image'),
        default='/athletes/default.png'
    )
    athlete = models.ForeignKey(Athlete, verbose_name=_('athlete'),
                                related_name='pictures', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _('picture')
        verbose_name_plural = _('pictures')


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


class Review(models.Model):
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

    def __str__(self):
        return f'{self.athlete.first_name} - {self.state}'

    class Meta:
        verbose_name = _('review')
        verbose_name_plural = _('reviews')
