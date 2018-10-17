from django.utils.translation import ugettext_lazy as _

from marketplace.emails.helpers import TemplateEmailMessage


class CampaignCreationEmail(TemplateEmailMessage):

    template_name = "emails/campaign_creation.html"
    default_subject = _("New campaign")


class CampaignApprovedEmail(TemplateEmailMessage):

    template_name = "emails/campaign_approved.html"
    default_subject = _("Campaign approved")


class CampaignReviewingEmail(TemplateEmailMessage):

    template_name = "emails/campaign_reviewing.html"
    default_subject = _("Campaign reviewing")


class CampaignRejectedEmail(TemplateEmailMessage):

    template_name = "emails/campaign_rejected.html"
    default_subject = _("Campaign rejected")
