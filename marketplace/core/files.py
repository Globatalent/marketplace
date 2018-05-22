# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.utils.deconstruct import deconstructible
from django.utils.text import slugify


@deconstructible
class UploadToDir(object):
    """Generates a function to give  to ``upload_to`` parameter in
    models.Fields, that generates an name for uploaded files based on ``populate_from``
    attribute.
    """

    def __init__(self, path, populate_from=None, prefix=None):
        self.path = path
        self.populate_from = populate_from
        self.prefix = prefix

    def __call__(self, instance, filename):
        """Generates a name for an uploaded file."""
        if self.populate_from is not None and not hasattr(instance, self.populate_from):
            raise AttributeError("Instance hasn't {} attribute".format(self.populate_from))
        ext = filename.split('.')[-1]
        readable_name = slugify(filename.split('.')[0])
        if self.populate_from:
            readable_name = slugify(getattr(instance, self.populate_from))
        file_name = f'{readable_name}.{ext}'
        if self.prefix is not None:
            file_name = f'{self.prefix}{file_name}'
        return os.path.join(self.path, file_name)
