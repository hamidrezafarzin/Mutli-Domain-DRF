import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from utils.errors.constants import Errors


def otp_validator(value):
    otp_length = settings.OTP_CONFIG["OTP_LENGTH"]
    OTP_PATTERN = rf"^[0-9]{{{otp_length}}}$"
    if not re.match(OTP_PATTERN, value):
        raise ValidationError(
            _(f"{Errors.INVALID_OTP_PATTERN}"),
        )
