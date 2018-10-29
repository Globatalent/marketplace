from django.utils.translation import ugettext_lazy as _


ATHLETE, CLUB = "athlete", "club"
CAMPAIGN_TYPES = ((ATHLETE, _("Athlete")), (CLUB, _("Club")))

APPROVED = "approved"
REJECTED = "rejected"
REVIEWING = "reviewing"
PENDING_REVIEW = "pending_review"
STATE_CHOICES = (
    (APPROVED, _("Approved")),
    (REJECTED, _("Rejected")),
    (REVIEWING, _("Reviewing")),
    (PENDING_REVIEW, _("Pending Review")),
)

MALE = "male"
FEMALE = "female"
SEX_CHOICES = ((MALE, _("Male")), (FEMALE, _("Female")))

FACEBOOK, INSTAGRAM, TWITTER, YOUTUBE, LINKEDIN, WHATSAPP, FLICKR = (
    "facebook",
    "instagram",
    "twitter",
    "youtube",
    "linkedin",
    "whatsapp",
    "flickr",
)
SOCIAL_NETWORKS = (
    (FACEBOOK, _("Facebook")),
    (INSTAGRAM, _("Instagram")),
    (TWITTER, _("Twitter")),
    (YOUTUBE, _("YouTube")),
    (LINKEDIN, _("LinkedIn")),
    (WHATSAPP, _("WhatsApp")),
    (FLICKR, _("Flickr")),
)
