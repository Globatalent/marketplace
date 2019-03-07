from django.utils.translation import ugettext_lazy as _

from marketplace.emails.helpers import TemplateEmailMessage


class PurchaseEmail(TemplateEmailMessage):

    template_name = "emails/purchase.html"
    default_subject = _("Thanks for your purchase!")
