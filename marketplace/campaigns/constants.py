from django.utils.translation import ugettext_lazy as _


ATHLETE, CLUB = "athlete", "club"
CAMPAIGN_TYPES = (
    (ATHLETE, _("Athlete")),
    (CLUB, _("Club")),
)

MALE = 'male'
FEMALE = 'female'
SEX_CHOICES = (
    (MALE, _('Male')),
    (FEMALE, _('Female'))
)

FACEBOOK, INSTAGRAM, TWITTER, YOUTUBE, LINKEDIN, TWITCH = \
    "facebook", "instagram", "twitter", "youtube", "linkedin", "twitch"
SOCIAL_NETWORKS = (
    (FACEBOOK, _("Facebook")),
    (INSTAGRAM, _("Instagram")),
    (TWITTER, _("Twitter")),
    (YOUTUBE, _("YouTube")),
    (LINKEDIN, _("LinkedIn")),
    (TWITCH, _("Twitch")),
)
