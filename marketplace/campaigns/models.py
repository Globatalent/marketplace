from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
from model_utils.models import TimeStampedModel

from marketplace.actions.constants import ADD_REVIEW
from marketplace.actions.decorators import dispatch_action
from marketplace.campaigns.constants import SEX_CHOICES, SOCIAL_NETWORKS, CAMPAIGN_TYPES, STATE_CHOICES, PENDING_REVIEW, \
    APPROVED, REJECTED, REVIEWING
from marketplace.campaigns.emails import CampaignApprovedEmail, CampaignReviewingEmail, CampaignRejectedEmail
from marketplace.campaigns.helpers import create_token
from marketplace.core.files import UploadToDir
from marketplace.purchases.constants import CURRENCY_CHOICES, USD


class Sport(TimeStampedModel):
    """List of available sports in the platform."""
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Campaign(TimeStampedModel):
    """An user can create a campaign. There are two kinds of campaigns:
    athlete and club.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="campaigns", on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=True, help_text=_("If the campaign is a draft it isn't complete"))
    kind = models.CharField(max_length=8, choices=CAMPAIGN_TYPES)
    state = models.CharField(choices=STATE_CHOICES, default=PENDING_REVIEW, max_length=20, verbose_name=_('state'))
    token = models.OneToOneField(
        "tokens.Token",
        related_name="campaign",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    # Card
    title = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = ThumbnailerImageField(
        max_length=250,
        upload_to=UploadToDir('campaigns', random_name=True),
        verbose_name=_('image'),
        null=True,
        blank=True
    )
    gender = models.CharField(choices=SEX_CHOICES, null=True, blank=True, max_length=20, verbose_name=_('sex'))
    sport = models.ForeignKey(
        "campaigns.Sport",
        related_name="campaigns",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    tags = models.ManyToManyField("tags.Tag", blank=True)

    # Content
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    club = models.CharField(max_length=128, null=True, blank=True)
    coach = models.CharField(max_length=128, null=True, blank=True)
    pitch_url = models.URLField(null=True, blank=True)
    pitch_image = ThumbnailerImageField(
        max_length=250,
        upload_to=UploadToDir('campaigns', random_name=True),
        null=True,
        blank=True
    )

    # Career
    ranking = models.CharField(max_length=128, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    achievements = models.TextField(null=True, blank=True)
    expected = models.TextField(null=True, blank=True)

    # Founding
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=USD)
    funds = models.FloatField(null=True, blank=True)
    use = models.TextField(null=True, blank=True)
    give_back = models.TextField(null=True, blank=True)
    examples = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title or str(self.id)

    def tag_names(self):
        return self.tags.values_list("name", flat=True)

    def send_state_changed_email(self):
        """Sends an email about the status change."""
        email_classes = {
            APPROVED: CampaignApprovedEmail,
            REVIEWING: CampaignReviewingEmail,
            REJECTED: CampaignRejectedEmail,
        }
        email = email_classes[self.state](context={'campaign': self})
        email.send()

    def save(self, *args, **kwargs):
        """Handles token creation when save."""
        is_insert = self.pk is None
        if not self.token and not self.is_draft and self.funds and self.funds > 0.0:
            self.token = create_token(self)
        if not is_insert:
            previous_campaign = Campaign.objects.get(pk=self.pk)
            if self.state != previous_campaign.state:
                self.send_state_changed_email()
        super().save(*args, **kwargs)


class Picture(models.Model):
    """Model to upload generic pictures, used by WYSWYG editors for campaign data."""
    campaign = models.ForeignKey("campaigns.Campaign", related_name="pictures", on_delete=models.CASCADE)
    image = ThumbnailerImageField(max_length=250, upload_to=UploadToDir('pictures', random_name=True))

    def __str__(self):
        return self.image


class Link(TimeStampedModel):
    """Link related with the campaign."""
    campaign = models.ForeignKey("campaigns.Campaign", related_name="links", on_delete=models.CASCADE)
    network = models.CharField(max_length=32, choices=SOCIAL_NETWORKS, null=True, blank=True)
    url = models.URLField(null=True, blank=True, verbose_name=_('url'))

    def __str__(self):
        return self.url or str(self.id)


class Revenue(TimeStampedModel):
    """Past revenues."""
    campaign = models.ForeignKey("campaigns.Campaign", related_name="revenues", on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=USD, blank=True)
    amount = models.FloatField()

    class Meta:
        unique_together = ("campaign", "year")


class Income(TimeStampedModel):
    """Future incomes."""
    campaign = models.ForeignKey("campaigns.Campaign", related_name="incomes", on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=USD, blank=True)
    amount = models.FloatField()

    class Meta:
        unique_together = ("campaign", "year")


class Recommendation(TimeStampedModel):
    campaign = models.ForeignKey("campaigns.Campaign", related_name="recommendations", on_delete=models.CASCADE)
    file = models.FileField(
        max_length=250,
        upload_to=UploadToDir('recommendations', random_name=True)
    )


class Review(TimeStampedModel):
    text = models.TextField(null=True, blank=True, verbose_name=_('text'))
    state = models.CharField(choices=STATE_CHOICES, default=PENDING_REVIEW, max_length=20, verbose_name=_('state'))
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True},
        verbose_name=_('user'),
        related_name="reviews"
    )
    campaign = models.ForeignKey(
        Campaign,
        related_name='reviews',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('review')
        verbose_name_plural = _('reviews')
        ordering = ("created", )
        unique_together = ('reviewer', 'campaign')

    def __str__(self):
        return self.campaign

    @dispatch_action(ADD_REVIEW, method=True)
    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)
        return result
