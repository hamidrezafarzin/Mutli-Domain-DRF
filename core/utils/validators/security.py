import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from utils.errors.constants import Errors


def xss_validator(value):
    XSS_PATTERN = r"(?i)<\s*(script|img|a|div|iframe|html|body|marquee|svg|embed|style|object|form|input|textarea|button|meta|link|base|frame|frameset|bgsound|layer|ilayer|bgsound|audio|video|source|applet|noframes|noscript|basefont|isindex|blink|xmp|plaintext|xml|object|head|title|slot)[^>]*>|on\w+\s*=\s*['\"]?[^'\"]*['\"]?|javascript\s*:\s*['\"]?[^'\"]*['\"]?"
    if re.search(XSS_PATTERN, value):
        raise ValidationError(
            _(f"{Errors.XSS_ATTACK_DETECTION}"),
        )
