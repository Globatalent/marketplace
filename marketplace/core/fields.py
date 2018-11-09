from django.db import models
from django.utils.translation import ugettext_lazy as _


class CountryCodeField(models.CharField):

    description = _("The alpha-2 code of a country, according to ISO 3166-1")

    def __init__(self, verbose_name=None, name=None, **kwargs):
        """Default max_length to 2 chars."""
        kwargs["max_length"] = kwargs.get("max_length", 2)
        super().__init__(verbose_name, name, **kwargs)

    def pre_save(self, model_instance, add):
        """Always upper."""
        value = super().pre_save(model_instance, add)
        return value.upper() if value else value
