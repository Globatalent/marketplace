from django.apps import AppConfig


class EmailsConfig(AppConfig):
    name = "marketplace.emails"
    verbose_name = "Emails"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        try:
            import emails.signals  # noqa F401
        except ImportError:
            pass
