from rest_framework.pagination import PageNumberPagination
from django.utils.translation import gettext_lazy as _


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 100
    limit_query_param = "limit"
    offset_query_param = "offset"
    offset_query_description = _("The initial index from which to return the results.")


class VerySmallResultsSetPagination(PageNumberPagination):
    page_size = 7
    page_size_query_param = "page_size"
    max_page_size = 7
    limit_query_param = "limit"
    offset_query_param = "offset"
    offset_query_description = _("The initial index from which to return the results.")
