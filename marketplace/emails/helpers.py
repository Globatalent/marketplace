import warnings

import bleach
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from options.models import Option

from marketplace.emails.tasks import send_email_asynchronously

from django.core.mail import send_mail


class TemplateEmailMessage(object):
    """An object to handle emails based on templates, with automatic plain
    alternatives.
    """

    template_name = None
    default_subject = ""
    default_from_email = None
    fake = False
    ##

    def __init__(self, to, subject=None, context=None, from_email=None, attaches=None):
        if self.template_name is None:
            warnings.warn("You have to specify the template_name")
        if not isinstance(to, list) and not isinstance(to, tuple):
            self.to = [to]
        self.subject = "%s" % self.default_subject if subject is None else subject
        self.from_email = self.default_from_email if from_email is None else from_email
        self.attaches = [] if attaches is None else attaches
        self.default_context = {} if context is None else context


    def get_context(self):
        """Hook to customize context."""
        # Add default context
        current_site = Site.objects.get_current()
        self.default_context.update(
            {
                "site": current_site,
                "frontend": Option.objects.get_value(
                    "FRONTEND_SITE_DOMAIN", current_site.domain
                ),
            }
        )
        return self.default_context

    def preview(self):
        """Renders the message for a preview."""
        context = self.get_context()
        message = render_to_string(self.template_name, context, using="django")
        return message

    def send(self, async=True):
        """Sends the email at the moment or using a Celery task."""
        if not settings.ENABLE_CUSTOM_EMAIL_SENDING:
            return
        context = self.get_context()
        message = render_to_string(self.template_name, context, using="django")
        message_txt = message.replace("\n", "")
        message_txt = message_txt.replace("</p>", "\n")
        message_txt = message_txt.replace("</h1>", "\n\n")
        message_txt = bleach.clean(message_txt, strip=True)


        if async and not self.fake:
            send_email_asynchronously.delay(
                self.subject, message_txt, message, self.from_email, self.to
            )
            if self.attaches:
                warnings.warn(
                    "Attaches will not added to the email, use async=False to send attaches."
                )
        elif not self.fake:
            email = EmailMultiAlternatives(
                subject=self.subject,
                body=message_txt,
                from_email=self.from_email,
                to=self.to,
            )
            send_mail(
                self.subject,
                message_txt,
                self.from_email,
                [self.to],
                fail_silently=False,
            )
            email.attach_alternative(message, "text/html")
            for attach in self.attaches:
                attach_file_name, attach_content, attach_content_type = attach
                email.attach(attach_file_name, attach_content, attach_content_type)
            email.send()


class AdminsTemplateEmailMessage(TemplateEmailMessage):
    """Emails only for admins."""

    def __init__(self, subject=None, context=None, from_email=None):
        to = [a[1] for a in settings.ADMINS]
        super().__init__(to, subject=subject, context=context, from_email=from_email)


class ManagersTemplateEmailMessage(TemplateEmailMessage):
    """Emails only for mangers."""

    def __init__(self, subject=None, context=None, from_email=None):
        to = [a[1] for a in settings.MANAGERS]
        super().__init__(to, subject=subject, context=context, from_email=from_email)
