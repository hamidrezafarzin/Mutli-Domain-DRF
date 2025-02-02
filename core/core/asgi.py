"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

env = os.environ.get("DJANGO_ENV", "production")
if env == "development":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.development")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.production")

application = get_asgi_application()
