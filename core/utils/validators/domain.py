import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def domain_validator(value):
    DOMAIN_PATTERN = r"^(?!:\/\/)([a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,6}$"
    # Check if the provided value does NOT match the domain pattern
    if not re.match(DOMAIN_PATTERN, value):
        raise ValidationError(
            _(f"Enter a valid domain name."),
        )