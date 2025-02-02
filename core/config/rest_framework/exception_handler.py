from django.core.exceptions import (
    ValidationError as DjangoValidationError,
    PermissionDenied,
)
from django.http import Http404

from rest_framework.views import exception_handler
from rest_framework import exceptions
from rest_framework.serializers import as_serializer_error


def drf_default_with_modifications_exception_handler(exc, ctx):
    # Convert DjangoValidationError to DRF's ValidationError
    if isinstance(exc, DjangoValidationError):
        exc = exceptions.ValidationError(as_serializer_error(exc))

    # Convert Http404 to DRF's NotFound
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()

    # Convert PermissionDenied to DRF's PermissionDenied
    if isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    response = exception_handler(exc, ctx)

    # If unexpected error occurs (server error, etc.)
    if response is None:
        return response

    # Ensure that the detail attribute is always a dictionary
    if not isinstance(exc.detail, dict):
        exc.detail = {"non_field_error": [exc.detail]}

    # Modify the response data based on the structure of the detail
    if isinstance(exc.detail, dict):
        response.data = {"detail": exc.detail}

    return response
