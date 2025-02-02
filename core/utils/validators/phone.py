import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from utils.errors.constants import Errors


def iranian_phone_validator(value):
    IRANIAN_PHONE_PATTERN = r"^09\d{9}$"
    if not re.match(IRANIAN_PHONE_PATTERN, value):
        raise ValidationError(
            _(f"{Errors.INVALID_PHONE_NUMBER_PATTERN}"),
        )
