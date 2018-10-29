# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.pagination import PageNumberPagination
from rest_framework.views import exception_handler


class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 300
