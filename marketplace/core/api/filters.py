# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import coreapi
import coreschema
from django.utils.encoding import force_text
from django.utils.translation import ugettext
from url_filter.integrations.drf import DjangoFilterBackend


class DjangoFilterDocs(DjangoFilterBackend):
    def get_schema_fields(self, view):
        assert (
            coreapi is not None
        ), "coreapi must be installed to use `get_schema_fields()`"
        assert (
            coreschema is not None
        ), "coreschema must be installed to use `get_schema_fields()`"

        fields = []
        if not getattr(view, "filter_fields", None):
            return fields
        for field in view.filter_fields:
            model_fields = list(
                filter(
                    lambda x: x.attname == field,
                    view.serializer_class.Meta.model._meta.fields,
                )
            )
            if model_fields:
                title = force_text(model_fields[0].verbose_name)
                if model_fields[0].help_text:
                    description = force_text(model_fields[0].help_text)
                else:
                    description = ugettext("Filter by {}").format(title)
                fields.append(
                    coreapi.Field(
                        name=field,
                        required=False,
                        location="query",
                        schema=coreschema.String(title=title, description=description),
                    )
                )
        return fields
